FROM python:3.9-slim

# Install dependencies
RUN pip install Flask

# Copy your app code
COPY app.py /app/app.py
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Run your app
CMD ["python", "app.py"]
