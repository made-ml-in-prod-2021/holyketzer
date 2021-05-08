import joblib
import json
import pandas as pd

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

MODEL_PATH = "model.pkl"
model = joblib.load(MODEL_PATH)

app = FastAPI()

@app.get("/health_check")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_class=JSONResponse)
async def predict(request: Request):
    df = pd.read_json(await request.json())
    predictions = model.predict(df)
    return json.dumps(list(map(int, predictions)))
