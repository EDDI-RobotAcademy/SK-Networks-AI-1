from pydantic import BaseModel

class KmeansClusterResponseForm(BaseModel):
    centers: list
    labels: list
    points: list