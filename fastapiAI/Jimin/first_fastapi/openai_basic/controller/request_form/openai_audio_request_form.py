from fastapi import UploadFile
from pydantic import BaseModel


class OpenAIAudioRequestForm(BaseModel):
    file: UploadFile