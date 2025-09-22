import requests

url = "https://ml-model-as-api-in-heroku-f4672dcf97cf.herokuapp.com/diabetes_prediction"

input_data_for_model = {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50,
}

# Send JSON directly
response = requests.post(url, json=input_data_for_model)

# Print JSON response
print(response.json())
