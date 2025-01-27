# Use an official Python image as the base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code and dependencies
COPY app.py /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI default port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]