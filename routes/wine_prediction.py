from fastapi import APIRouter
from models.prediction_query import PredictionQuery
from models.prediction_output import PredictionOutput
from typing_extensions import Annotated
from fastapi import Query

from services.get_wine_prediction import get_single_prediction

router = APIRouter()

@router.get("/predict_wine")
def predict_wine(param_query: Annotated[PredictionQuery, Query()]) -> PredictionOutput:
    try:
        res = get_single_prediction(param_query)
        return res

    except:
        raise Exception


