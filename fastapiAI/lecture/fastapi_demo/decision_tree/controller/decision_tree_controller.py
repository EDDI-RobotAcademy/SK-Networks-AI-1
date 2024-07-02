import os

from fastapi import APIRouter, Depends, HTTPException, status

from decision_tree.controller.request_form.wine_feature_request_form import WineFeatureRequestForm
from decision_tree.service.decision_tree_service_impl import DecisionTreeServiceImpl
from joblib import load

import pandas as pd

decisionTreeRouter = APIRouter()

FEATURE_NAMES_PATH = 'wine_feature_name.joblib'
TARGET_NAMES_PATH = 'wine_target_name.joblib'
TRAINED_MODEL_PATH = 'wine_trained_model.h5'


async def injectDecisionTreeService() -> DecisionTreeServiceImpl:
    return DecisionTreeServiceImpl()


@decisionTreeRouter.get("/decision-tree-train")
async def decisionTreeTrain(decisionTreeService: DecisionTreeServiceImpl =
                               Depends(injectDecisionTreeService)):

    print(f"controller -> decisionTreeTrain()")

    decisionTreeService.decisionTreeTrain()
def load_model():
    if os.path.exists(TRAINED_MODEL_PATH):
        return load(TRAINED_MODEL_PATH)
    else:
        raise HTTPException(status_code=404, detail="Model not found. Please train the model first.")

# 특성 이름 로드 함수
def load_feature_names():
    if os.path.exists(FEATURE_NAMES_PATH):
        return load(FEATURE_NAMES_PATH)
    else:
        raise HTTPException(status_code=404, detail="Feature names not found. Please train the model first.")

def load_target_names():
    if os.path.exists(TARGET_NAMES_PATH):
        return load(TARGET_NAMES_PATH)
    else:
        raise HTTPException(status_code=404, detail="Target names not found. Please train the model first.")


# 긴급하므로 일단 동작하게 만듬
@decisionTreeRouter.post("/decision-tree-predict")
async def decisionTreePredict(wineFeatureRequestForm: WineFeatureRequestForm):
    model = load_model()
    feature_names = load_feature_names()
    target_names = load_target_names()

    inputData = pd.DataFrame([
        [
            feature_names.alcohol, feature_names.malic_acid, feature_names.ash, feature_names.alcalinity_of_ash,
            feature_names.magnesium, feature_names.total_phenols, feature_names.flavanoids,
            feature_names.nonflavanoid_phenols, feature_names.proanthocyanins,
            feature_names.color_intensity, feature_names.hue, feature_names.od280_od315_of_diluted_wines,
            feature_names.proline
         ]
    ], columns=feature_names)

    predictions = model.predict(inputData)
    predictedClass = int(predictions[0].argmax())
    predictedClassName = target_names[predictedClass]

    return {"predicted_class": predictedClass, "predicted_class_name": predictedClassName}
