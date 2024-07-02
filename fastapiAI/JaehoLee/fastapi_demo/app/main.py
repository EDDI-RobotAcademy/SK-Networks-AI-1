import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from async_db.database import getMySqlPool, createTableIfNeccessary
from decision_tree.controller.decision_tree_controller import decisionTreeRouter
from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from gradient_descent.controller.gradient_descent_controller import gradientDescentRouter
from kmeans.controller.kmeans_controller import kmeansRouter
from logistic_regression.controller.logistic_regression_controller import logisticRegressionRouter
from orders_analysis.controller.orders_analysis_controller import ordersAnalysisRouter
from polynomialRegression.controller.polynomial_regression_controller import polynomialRegressionRouter
from random_forest.controller.random_forest_controller import randomForestRouter
from tf_iris.controller.tf_iris_controller import tfIrisRouter
from train_test_evaluation.controller.train_test_evaluation_controller import trainTestEvaluationRouter

import warnings

async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(logisticRegressionRouter)
app.include_router(trainTestEvaluationRouter)
app.include_router(polynomialRegressionRouter)
app.include_router(exponentialRegressionRouter)
app.include_router(randomForestRouter)
app.include_router(kmeansRouter)
app.include_router(tfIrisRouter)
app.include_router(ordersAnalysisRouter)
app.include_router(gradientDescentRouter)
app.include_router(decisionTreeRouter)

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
    uvicorn.run(app, host="localhost", port=33333)
