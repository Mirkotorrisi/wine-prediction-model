from pydantic import BaseModel, Field

class PredictionOutput(BaseModel):
    """
    Represents the output of a prediction.
    """
    prediction: str = Field(...)
    probability: float = Field(..., description="Predicted probability")