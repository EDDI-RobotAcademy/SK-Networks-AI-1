import uvicorn
from fastapi import  FastAPI

from logistic_regiession_controller.logistic_regiession_controller import logisticRegiessionRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

app.include_router(logisticRegiessionRouter)

if __name__ == "__main__":
    import uvirorn
    uvicorn.run(app, host="127.0.0.1", port= 33333)