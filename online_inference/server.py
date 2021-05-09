import joblib
import json
import pandas as pd

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

MODEL_PATH = "model.pkl"
model = joblib.load(MODEL_PATH)

FEATURES = [
  "age",
  "sex",
  "cp",
  "trestbps",
  "chol",
  "fbs",
  "restecg",
  "thalach",
  "exang",
  "oldpeak",
  "slope",
  "ca",
  "thal",
]

app = FastAPI()

@app.get("/health_check")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_class=JSONResponse)
async def predict(request: Request):
    df = pd.DataFrame(await request.json())

    if set(df.columns) != set(FEATURES):
        raise HTTPException(
          status_code=400,
          detail="Exactly these features are excepeted: " + ", ".join(FEATURES),
        )
        # raise RequestValidationError("Exactly these features are excepeted: " + ", ".join(FEATURES))

    predictions = model.predict(df)
    return json.dumps(list(map(int, predictions)))
