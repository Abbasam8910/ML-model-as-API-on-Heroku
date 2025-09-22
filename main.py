from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

# Allow all origins (for testing or frontend use)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Load the saved model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# Root route (fixes 404 when visiting the base URL)
@app.get("/")
def root():
    return {"message": "Welcome to the Diabetes Prediction API"}

# Prediction route
@app.post("/diabetes_prediction")
def diabetes_pred(input_parameters: ModelInput):
    input_dict = input_parameters.dict()

    input_list = [
        input_dict["Pregnancies"],
        input_dict["Glucose"],
        input_dict["BloodPressure"],
        input_dict["SkinThickness"],
        input_dict["Insulin"],
        input_dict["BMI"],
        input_dict["DiabetesPedigreeFunction"],
        input_dict["Age"],
    ]

    prediction = diabetes_model.predict([input_list])

    result = "The person is Diabetic" if prediction[0] == 1 else "The person is not Diabetic"
    return {"prediction": result}
