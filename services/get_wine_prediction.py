# from sklearn.datasets import load_wine
from typing_extensions import Annotated
from fastapi import Query
from models.prediction_query import PredictionQuery
from models.prediction_output import PredictionOutput

import numpy as np
import joblib


# wine_data = load_wine()

# target_names = wine_data.target_names
target_names = ['class_0', 'class_1', 'class_2']

with open("assets/wine_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)

def get_single_prediction(query: Annotated[PredictionQuery, Query()]) -> PredictionOutput:
    '''Get a single wine prediction based on the provided query parameters.'''
    current_record = np.array([
        query.alcohol,
        query.malic_acid,
        query.ash,
        query.alcalinity_of_ash,
        query.magnesium,
        query.total_phenols,
        query.flavanoids,
        query.nonflavanoid_phenols,
        query.proanthocyanins,
        query.color_intensity,
        query.hue,
        query.od280_od315_of_diluted_wines,
        query.proline
    ])

    record_reshape = current_record.reshape(1,-1)

    predicted_proba = model.predict_proba(record_reshape)[0]
    predicted_class = model.predict(record_reshape)[0]

    predicted_proba_dict = {target_names[i]: predicted_proba[i] for i in range(len(predicted_proba))}

    predicted_class_name = target_names[predicted_class]

    return PredictionOutput(prediction=predicted_class_name, probability=predicted_proba_dict[predicted_class_name])
