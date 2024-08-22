import os

import httpx
# pip install faiss-cpu
import faiss
import numpy as np

from dotenv import load_dotenv
from fastapi import HTTPException

import openai


from openai_basic.repository.openai_basic_repository import OpenAIBasicRepository
from motor.motor_asyncio import AsyncIOMotorDatabase


load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')
if not openaiApiKey:
    raise ValueError('API Key가 준비되어 있지 않습니다!')

class OpenAIBasicRepositoryImpl(OpenAIBasicRepository):
    SIMILARITY_TOP_RANK = 3

    headers = {
        'Authorization': f'Bearer {openaiApiKey}',
        'Content-Type': 'application/json'
    }

    OPENAI_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"

    def __init__(self, vectorDbPool: AsyncIOMotorDatabase):
        self.vectorDbPool = vectorDbPool

    async def generateText(self, userSendMessage):
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {"role": "system", "content": "You are a helpful assitant."},
                {"role": "user", "content": userSendMessage}
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.OPENAI_CHAT_COMPLETIONS_URL, headers=self.headers, json=data)
                response.raise_for_status()

                return response.json()['choices'][0]['message']['content'].strip()

            except httpx.HTTPStatusError as e:
                print(f"HTTP Error: {str(e)}")
                print(f"Status Code: {e.response.status_code}")
                print(f"Response Text: {e.response.text}")
                raise HTTPException(status_code=e.response.status_code, detail=f"HTTP Error: {e}")

            except (httpx.RequestError, ValueError) as e:
                print(f"Request Error: {e}")
                raise HTTPException(status_code=500, detail=f"REquest Error: {e}")

    def sentimentAnalysis(self, userSendMessage):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. 한글로 답변하자!"},
                {"role": "user", "content": f"Analyze the sentiment of the following text:\n\n{userSendMessage}"}
            ]
        )
        print(f"openai response: {response.json()}")
        return response.choices[0].message.content.strip()

    def audioAnalysis(self, audioFile):
        try:
            # 임시 파일 저장
            file_location = f"temp_{audioFile.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(audioFile.file.read())

            # Whisper API 호출
            with open(file_location, "rb") as file:
                transcript = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=file
                )

            # 임시 파일 삭제
            os.remove(file_location)
            print(f"transcript: {transcript}")

            # return transcript['text']
            return transcript.text

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    def embeddingList(self):
        return self.vectorDbPool['embeddings']

    def openAiBasedEmbedding(self, paperTitleList):
        response = openai.embeddings.create(
            input=paperTitleList,
            model="text-embedding-ada-002"
        )

        print(f"response: {response}")
        return response.data[0].embedding

    def createL2FaissIndex(self, embeddingVectorDimension):
        return faiss.IndexFlatL2(embeddingVectorDimension)

    def similarityAnalysis(self, userRequestPaperTitle, faissIndex):
        embeddingUserRequest = np.array(
            self.openAiBasedEmbedding(userRequestPaperTitle)).astype('float32').reshape(1, -1)
        distanceList, indexList = faissIndex.search(embeddingUserRequest, self.SIMILARITY_TOP_RANK)

        return indexList[0], distanceList[0]
