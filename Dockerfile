FROM python:3.9-slim

# Install Flask and requests
RUN pip install Flask requests

# Copy the Python application
COPY app.py /app/app.py
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
