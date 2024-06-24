import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from async_db.database import getMySqlPool, createTableIfNeccessary
from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from polynomialRegression.controller.polynomial_regression_controller import polynomialRegressionRouter
from post.controller.post_controller import postRouter
from train_test_evaluation.controller.train_test_evaluation import trainTestEvaluationRouter

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.db_pool = await getMySqlPool()
    await createTableIfNeccessary(app.state.db_pool)

@app.on_event("shutdown")
async def shutdown_event():
    app.state.db_pool.close()
    await app.state.db_pool.wait_closed()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)
app.include_router(exponentialRegressionRouter)
app.include_router(postRouter, prefix="/post")

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=33333)