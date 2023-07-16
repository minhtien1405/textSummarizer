from fastapi import FastAPI
import uvicorn
import sys
import os

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline



text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def trainning():
  try:
    os.system("python main.py")
    return Response("Trainning Triggered!")
  
  except Exception as e:
      print(e)
      return Response(f"Trainning Failed! {e}")


@app.post("/predict")
async def predict_route(text:str):
  try:
    prediction = PredictionPipeline().predict(text)
    return Response(prediction)
  
  except Exception as e:
      print(e)
      return Response(f"Prediction Failed! {e}")

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)