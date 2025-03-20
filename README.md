# 📧 Spam Email Classification - Multi-Model Flask App 🚀

## 🔥 Predict whether an email is spam or not using multiple machine learning models!

This project provides a **Flask-based web application** that allows users to:
✅ Choose between different **Machine Learning models** (SVM, Random Forest, Naive Bayes, etc.)  
✅ Predict whether an email is **Spam** or **Not Spam**  
✅ Use an **API endpoint** to get predictions programmatically  
✅ Visualize data with **WordClouds** and accuracy charts  

---

## 📸 Demo & Screenshots

### 🌍 Web Interface
![App Screenshot](screenshots/ui.png)

### 📊 WordCloud Visualization
**Ham Emails:**  
![Ham WordCloud](screenshots/ham_wordcloud.png)

**Spam Emails:**  
![Spam WordCloud](screenshots/spam_wordcloud.png)

### 📈 Model Performance Comparison
![Model Performance](screenshots/model_comparison.png)

---

## ✨ Features
- 🔥 **Multi-Model Support**: Choose from SVM, Random Forest, Naive Bayes, KNN, and Decision Tree.
- 🌍 **Flask Web Interface**: A simple and interactive UI for email classification.
- 🔄 **REST API Support**: Get predictions via an API endpoint.
- 🎨 **Data Visualization**: Includes word cloud generation for spam vs. ham emails.
- 📊 **Model Performance Analysis**: Compare accuracy across models.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/spam-classifier.git
cd spam-classifier
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application
```bash
python app.py
```

The Flask app should now be accessible at **http://127.0.0.1:5000/**.

---

## 🚀 Usage

### 🌍 Web Interface
- Enter the email text in the input field.
- Select a machine learning model from the dropdown.
- Click **Predict** to classify the email.

### 🔄 API Endpoint
You can also make predictions via API:

#### Request:
```bash
curl -X POST "http://127.0.0.1:5000/api/predict" -H "Content-Type: application/json" -d '{"email": "Win a lottery now!", "model": "Naive Bayes"}'
```

#### Response:
```json
{
    "email": "Win a lottery now!",
    "model": "Naive Bayes",
    "prediction": "Spam"
}
```

---

## 📂 Dataset & Preprocessing
- The dataset consists of labeled spam and ham (non-spam) emails.
- **Preprocessing steps:**
  - Removing unnecessary columns
  - Converting spam labels to binary (0 = Ham, 1 = Spam)
  - Text vectorization using CountVectorizer

---

## 🔬 Machine Learning Models Used
- **Naive Bayes** 🧠
- **Support Vector Machine (SVM)** ⚡
- **K-Nearest Neighbors (KNN)** 🔎
- **Decision Tree** 🌲
- **Random Forest** 🌳🌳🌳

Each model is trained using email text data and evaluated based on accuracy scores.

---

## 🏗 Project Structure
```
📁 spam-classifier/
│-- 📂 models/             # Pre-trained models (saved as .pkl files)
│-- 📂 static/             # CSS, JS, and images for the web UI
│-- 📂 templates/          # HTML templates
│-- ├── index.html        # Main web UI
│-- ├── app.py            # Flask app
│-- ├── main.py           # Entry point for Hugging Face deployment
│-- ├── utils.py          # Helper functions for loading models and making predictions
│-- ├── requirements.txt  # Required libraries
│-- ├── README.md         # This file
```

---

## 🤝 Contributing
Pull requests are welcome! Please open an issue for any feature requests or bugs.

---

## 📜 License
MIT License - Use this project freely for educational and personal purposes.

---

### 🎯 Developed by **Your Name**

