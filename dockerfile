# Use an official lightweight Python image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install system dependencies if needed
RUN apt-get update -y && apt-get install -y --no-install-recommends gcc

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
