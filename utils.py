# utils.py (Helper Functions)
import pickle
import os
from pathlib import Path

MODELS = {
    'Support Vector Machine': 'Models/svm_model.pkl',
    'Random Forest': 'Models/rf_model.pkl',
    'K-Nearest Neighbors': 'Models/knn_model.pkl',
    'Naive Bayes': 'Models/clf_NaiveBaised.pkl',
    'Decision Tree': 'Models/DT_model.pkl'
}


def get_available_models():
    """
    Returns a list of available models
    """
    return list(MODELS.keys())


def load_model(model_name):
    """
    Loads the specified model from file.
    """
    if model_name not in MODELS:
        raise ValueError(f"Model {model_name} not found")

    model_file = MODELS[model_name]
    try:
        with open(model_file, "rb") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file {model_file} not found")
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")


def model_predict(email, model_name):
    """
    Predicts using the specified model.
    """
    try:
        model = load_model(model_name)
        prediction = model.predict([email])
        return 1 if prediction[0] == 1 else -1
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")
