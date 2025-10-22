# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask redis gunicorn

# Expose the Flask port
EXPOSE 5000

# Run Flask app with Gunicorn (production-grade WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
