# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

RUN pip install flask redis


# Run Flask app
CMD ["python", "app.py"]
