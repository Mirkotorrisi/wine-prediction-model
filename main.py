from fastapi import FastAPI
from routes import wine_prediction


app = FastAPI(debug=True, title="Wine prediction model API", description="API for managing wine predictions", version="1.0.0")

app.include_router(wine_prediction.router, prefix="/wine", tags=["Wine"])