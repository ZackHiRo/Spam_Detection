from app import app

if __name__ == "__main__":
    # Use port 7860 for Hugging Face Spaces
    app.run(host="0.0.0.0", port=7860, debug=True)