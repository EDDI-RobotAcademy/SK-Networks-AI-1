from fastapi import FastAPI, File, UploadFile, APIRouter
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch
import io

multiModalRouter = APIRouter()

# 모델 및 프로세서 로드
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@multiModalRouter.post("/caption")
async def generate_caption(image: UploadFile = File(...)):
    try:
        # 이미지를 PIL 이미지로 변환
        image_bytes = await image.read()
        img = Image.open(io.BytesIO(image_bytes))

        # 이미지 전처리
        pixel_values = feature_extractor(images=img, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        # 캡션 생성
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return {"caption": caption}

    except Exception as e:
        return {"error": str(e)}
