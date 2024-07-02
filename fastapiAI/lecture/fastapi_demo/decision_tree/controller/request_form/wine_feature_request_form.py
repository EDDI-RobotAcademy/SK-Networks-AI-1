from pydantic import BaseModel


class WineFeatureRequestForm(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
