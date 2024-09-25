import os

from dotenv import load_dotenv
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from openai import OpenAI
from pydantic import BaseModel

imageGenerationRouter = APIRouter()

load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')

class ImageGenerationRequestForm(BaseModel):
    userRequestDescription :str

client = OpenAI(api_key=openaiApiKey)


@imageGenerationRouter.post("/request-image-generation")
async def requestImageGeneration(imageGenerationRequestForm: ImageGenerationRequestForm):
    print(f"controller -> requestImageGeneration(): imageGenerationRequestForm: {imageGenerationRequestForm}")

    # imageGenerationRequestForm으로 받은 userRequestDescription을 prompt에 배치해야 하는데 직접 다 적어버림
    generatedImageURL = client.images.generate(
        prompt=("A highly detailed, high-resolution 3D rendering of a medieval siege."
                "The scene features a vast undead army attacking a human castle."
                "At the forefont, a menacing Death Knight in dark, intricately detailed armor, with a chilling aura and glowing eyes, leads the charge."
                "The Death Knight should have a commanding presence, with a dark and intimidating demeanor."
                "The undead soldiers are skeletons and ghostly creatures, shown with clear, realistic bone textures and spectral features."
                "The human castle is engulfed in intense flames, with realistic fire, thick smoke, and collapsing walls."
                "The scene should include dynamic lightning, detailed textures, and a scene of overwhelming destruction and chaos."),
        # 사진을 몇장 뽑을 것인지, 너무 적게 뽑으면 잘 안나올 수 있다.
        n=5,
        size="1024x1024"
    )

    print("Generated Image URL:", generatedImageURL)

    return JSONResponse(content=generatedImageURL, status_code=status.HTTP_200_OK)