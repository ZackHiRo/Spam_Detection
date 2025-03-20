FROM python:3.11-slim

WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir flask gunicorn numpy pandas scikit-learn

# Copy application files
COPY . .

# Make sure the Models directory exists
RUN mkdir -p Models

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "main:app"]
