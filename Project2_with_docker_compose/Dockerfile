# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install FastAPI, Uvicorn, and any other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app into the container
COPY . /app

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
