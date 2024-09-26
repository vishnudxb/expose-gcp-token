# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install required Python packages
RUN pip install Flask requests

# Copy the Python script
COPY app.py /app/app.py

# Set the working directory
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]

