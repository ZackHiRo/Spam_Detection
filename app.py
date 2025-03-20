# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from utils import model_predict, get_available_models

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    models = get_available_models()
    return render_template("index.html", models=models)

@app.route('/predict', methods=["POST"])
def predict():
    """
    Handles form submission and returns prediction.
    """
    email = request.form.get('email')
    model_name = request.form.get('model')
    
    if not email:
        return render_template("index.html", 
                             error="Please provide an email",
                             models=get_available_models())

    if not model_name:
        return render_template("index.html", 
                             error="Please select a model",
                             models=get_available_models())

    try:
        prediction = model_predict(email, model_name)
        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template("index.html", 
                             prediction=result,
                             email=email,
                             selected_model=model_name,
                             models=get_available_models())
    except Exception as e:
        return render_template("index.html", 
                             error=f"Error: {str(e)}",
                             models=get_available_models())

@app.route('/api/predict', methods=["POST"])
def predict_api():
    """
    API endpoint that accepts a JSON payload and returns a prediction.
    """
    try:
        data = request.get_json()
        email = data.get("email")
        model_name = data.get("model")
        
        if not email:
            return jsonify({'error': 'No email provided'}), 400

        if not model_name:
            return jsonify({'error': 'No model selected'}), 400

        prediction = model_predict(email, model_name)
        result = "Spam" if prediction == 1 else "Not Spam"
        return jsonify({
            'email': email,
            'model': model_name,
            'prediction': result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
