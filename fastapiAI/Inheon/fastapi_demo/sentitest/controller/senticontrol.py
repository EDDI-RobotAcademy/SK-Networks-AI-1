import os
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
import re
from keras.models import Sequential, load_model
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.callbacks import ModelCheckpoint
import numpy as np
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords

naturalLanguageProcessingRouter = APIRouter()

# 전역 변수
english_stops = set(stopwords.words('english'))
model_file_path = os.path.join(os.getcwd(), "models", "LSTM.h5")
token = Tokenizer(lower=False)


# 데이터 로드 및 전처리
def load_dataset():
    df = pd.read_csv('../assets/IMDB Dataset.csv')
    x_data = df['review']  # 리뷰 텍스트
    y_data = df['sentiment']  # 감정 레이블

    # 리뷰 전처리
    x_data = x_data.replace({'<.*?>': ''}, regex=True)
    x_data = x_data.replace({'[^A-Za-z]': ' '}, regex=True)
    x_data = x_data.apply(lambda review: [w for w in review.split() if w not in english_stops])  # 불용어 제거
    x_data = x_data.apply(lambda review: [w.lower() for w in review])  # 소문자로 변환

    # 감정 레이블 인코딩 (positive -> 1, negative -> 0)
    y_data = y_data.replace('positive', 1)
    y_data = y_data.replace('negative', 0)

    print(f"x_data: {x_data}, y_data: {y_data}")

    return x_data, y_data


# 데이터 전처리 API
@naturalLanguageProcessingRouter.get("/load-data")
async def load_data(background_tasks: BackgroundTasks):
    background_tasks.add_task(load_and_preprocess_data)
    return JSONResponse(content={"message": "Data loading and preprocessing started in background."})


def load_and_preprocess_data():
    try:
        global x_train, x_test, y_train, y_test, max_length, total_words
        x_data, y_data = load_dataset()
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)

        # 토큰화 및 패딩
        token.fit_on_texts(x_train)
        x_train = token.texts_to_sequences(x_train)
        x_test = token.texts_to_sequences(x_test)

        max_length = get_max_length(x_train)
        x_train = pad_sequences(x_train, maxlen=max_length, padding='post', truncating='post')
        x_test = pad_sequences(x_test, maxlen=max_length, padding='post', truncating='post')

        total_words = len(token.word_index) + 1
        print("Data loading and preprocessing completed.")
    except Exception as e:
        print(f"Error during data loading and preprocessing: {e}")


# 리뷰 최대 길이 계산 함수
def get_max_length(reviews):
    review_length = [len(review) for review in reviews]
    return int(np.ceil(np.mean(review_length)))


# 모델 학습 및 저장 API
@naturalLanguageProcessingRouter.get("/train-model")
async def train_model():
    global x_train, y_train, model_file_path
    if 'x_train' not in globals():
        return JSONResponse(content={"message": "Data not loaded. Load data first."}, status_code=404)

    try:
        EMBED_DIM = 32
        LSTM_OUT = 64
        model = Sequential()
        model.add(Embedding(total_words, EMBED_DIM, input_length=max_length))
        model.add(LSTM(LSTM_OUT))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        checkpoint = ModelCheckpoint(model_file_path, monitor='accuracy', save_best_only=True, verbose=1)

        model.fit(x_train, y_train, epochs=5, batch_size=128, callbacks=[checkpoint])

        return JSONResponse(content={"message": "Model trained and saved."})
    except Exception as e:
        print(f"Error during model training: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# 예측 API
@naturalLanguageProcessingRouter.get("/predict")
async def predict(text: str):
    try:
        if not os.path.exists(model_file_path):
            raise HTTPException(status_code=404, detail="Model not found. Train the model first.")

        model = load_model(model_file_path)
        preprocessed_text = preprocess_text(text)
        tokenize_words = token.texts_to_sequences([preprocessed_text])
        tokenize_words = pad_sequences(tokenize_words, maxlen=max_length, padding='post', truncating='post')

        result = model.predict(tokenize_words)
        sentiment = "positive" if result >= 0.7 else "negative"

        return JSONResponse(content={"sentiment": sentiment})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def preprocess_text(text):
    text = re.sub(r'<.*?>', '', text)  # HTML 태그 제거
    text = re.sub(r'[^A-Za-z\s]', '', text)  # 알파벳 외 문자 제거
    words = text.split(' ')
    filtered = [w for w in words if w not in english_stops]
    return ' '.join(filtered).lower()