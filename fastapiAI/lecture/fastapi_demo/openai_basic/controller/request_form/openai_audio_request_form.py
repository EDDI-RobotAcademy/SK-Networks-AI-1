from pydantic import BaseModel
from fastapi import UploadFile, File

class OpenAIAudioRequestForm(BaseModel):
    file: UploadFile
