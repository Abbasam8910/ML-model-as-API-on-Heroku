# 🩺 Diabetes Prediction API

A machine learning-powered REST API that predicts diabetes risk based on patient health metrics. Built with FastAPI and scikit-learn, deployed on Heroku for easy access and integration.

## 🎯 Overview

This project implements a Support Vector Machine (SVM) model trained on the PIMA Indian Diabetes Dataset to predict whether a person is diabetic based on various health parameters. The model is exposed through a FastAPI web service that can be easily integrated into healthcare applications, websites, or other systems.

## ✨ Features

- **Machine Learning Model**: SVM classifier trained on PIMA Diabetes Dataset
- **REST API**: FastAPI-based web service with automatic documentation
- **CORS Support**: Cross-origin resource sharing enabled for frontend integration
- **Input Validation**: Pydantic models ensure data integrity
- **Cloud Deployment**: Deployed on Heroku for global accessibility
- **Easy Integration**: Simple HTTP POST requests for predictions

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client App    │───▶│   FastAPI       │───▶│   ML Model      │
│                 │    │   Web Server    │    │   (SVM)         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📊 Dataset Information

The model is trained on the **PIMA Indian Diabetes Dataset** which contains:

- **768 samples** of patient data
- **8 input features** (health metrics)
- **Binary classification** (diabetic/non-diabetic)

### Input Features:

1. **Pregnancies**: Number of pregnancies
2. **Glucose**: Plasma glucose concentration (mg/dL)
3. **BloodPressure**: Diastolic blood pressure (mm Hg)
4. **SkinThickness**: Triceps skin fold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg/(height in m)^2)
7. **DiabetesPedigreeFunction**: Diabetes pedigree function
8. **Age**: Age in years

## 🚀 API Endpoints

### Base URL

```
https://ml-model-as-api-in-heroku-f4672dcf97cf.herokuapp.com/
```

### Endpoints

#### `GET /`

Welcome endpoint that returns basic API information.

**Response:**

```json
{
  "message": "Welcome to the Diabetes Prediction API"
}
```

#### `POST /diabetes_prediction`

Predicts diabetes based on input health parameters.

**Request Body:**

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

**Response:**

```json
{
  "prediction": "The person is Diabetic"
}
```

## 💻 Local Development

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Abbasam8910/ML-model-as-API-on-Heroku.git
   cd ML-model-as-API-on-Heroku
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**
   - API: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

### Testing the API

Use the provided `api_implementation.py` script to test the API:

```bash
python api_implementation.py
```

Or use curl:

```bash
curl -X POST "http://localhost:8000/diabetes_prediction" \
     -H "Content-Type: application/json" \
     -d '{
       "Pregnancies": 6,
       "Glucose": 148,
       "BloodPressure": 72,
       "SkinThickness": 35,
       "Insulin": 0,
       "BMI": 33.6,
       "DiabetesPedigreeFunction": 0.627,
       "Age": 50
     }'
```

## 🔬 Model Development

The machine learning model development process is documented in the Jupyter notebook `Diabetes Model for API.ipynb`, which includes:

1. **Data Loading & Exploration**

   - Loading the PIMA Diabetes Dataset
   - Statistical analysis and data visualization
   - Missing value analysis

2. **Data Preprocessing**

   - Feature scaling and normalization
   - Train-test split (80-20)

3. **Model Training**

   - Support Vector Machine (SVM) implementation
   - Model training and validation

4. **Model Evaluation**

   - Accuracy metrics
   - Performance analysis

5. **Model Serialization**
   - Saving trained model using pickle
   - Model loading and testing

## 🗂️ File Structure

```
├── main.py                          # FastAPI application
├── api_implementation.py            # API testing script
├── diabetes_model.sav              # Trained ML model (pickle)
├── diabetes.csv                    # Training dataset
├── Diabetes Model for API.ipynb   # Model development notebook
├── requirements.txt                # Python dependencies
├── Procfile                       # Heroku deployment configuration
├── README.md                      # Project documentation
└── LICENSE                        # MIT License
```

## 🛠️ Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for FastAPI
- **Heroku**: Cloud platform for deployment

## 🚀 Deployment

The application is configured for easy deployment on Heroku:

1. **Heroku Configuration:**

   - `Procfile`: Specifies the web server command
   - `requirements.txt`: Lists all Python dependencies

2. **Environment Variables:**

   - No additional environment variables required

3. **Automatic Deployment:**
   - Push to main branch triggers automatic deployment
   - Health checks ensure API availability

## 📈 Model Performance

The SVM model demonstrates reliable performance for diabetes prediction based on the PIMA dataset features. Key metrics and performance details can be found in the Jupyter notebook.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PIMA Indian Diabetes Dataset**: National Institute of Diabetes and Digestive and Kidney Diseases
- **FastAPI Community**: For excellent documentation and support
- **Heroku**: For providing reliable cloud hosting

## 📞 Contact

**Abbas Ahmad**

- GitHub: [@Abbasam8910](https://github.com/Abbasam8910)
- Repository: [ML-model-as-API-on-Heroku](https://github.com/Abbasam8910/ML-model-as-API-on-Heroku)

---

⭐ **Star this repository if you found it helpful!**
