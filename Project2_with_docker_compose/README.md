# Project 2 - With Docker Compose Application

To run your FastAPI app with multiple instances using Docker Compose, you need to set up a Dockerfile to containerize the app and a `docker-compose.yml` file to define how the app should scale.


### FastAPI File  : main.py

```
from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    server_name = socket.gethostname()  # Get the server/instance ID
    return {"message": f"Hello, from server : {server_name}"}
```

### Dockerfile
The `Dockerfile` will define the steps to build the container, install the necessary dependencies, and run your FastAPI app.

```dockerfile
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

```

### requirements.txt
Since you’re using FastAPI and Uvicorn, you'll need to list those dependencies in `requirements.txt`.

```txt
fastapi
uvicorn
```

### Docker Compose File (`docker-compose.yml`)

To scale the app to 3 instances, you need to set up Docker Compose with the appropriate service configuration.

```yaml
services:
  fastapi:
    build: .
    ports:
      - "8000"  # Dynamically map container port 8000 to a random host port
    deploy:
      replicas: 3  # Scaling to 3 instances
    networks:
      - fastapi-network
    environment:
      - UVICORN_CMD=uvicorn main:app --host 0.0.0.0 --port 8000

networks:
  fastapi-network:
    driver: bridge
```

### Steps to Run Your Application

1. **Build the Docker Image:**
   In the directory containing your `Dockerfile`, `docker-compose.yml`, and `requirements.txt`, run the following command to build your Docker image:

   ```bash
   docker-compose build
   ```

2. **Run the Application in Docker Compose:**
   To start the application with 3 instances, run:

   ```bash
   docker-compose up
   ```

   This will scale the FastAPI service to 3 replicas as defined in the `docker-compose.yml` file.

3. **Verify the Application:**
   After running `docker-compose up`, you can access the FastAPI application at `http://localhost:8000`. Since you’ve scaled to 3 replicas, each replica will handle requests. You can check the instance from which the response is being served by looking at the `server_name` in the response.

---

With this setup, you have a containerized FastAPI app with multiple instances that can be scaled with Docker Compose.


### Accessing application using CURL Command

To send a `curl` command to get a response from your FastAPI application running in Docker, you need to access the dynamically assigned ports on your host machine. 

Since your Docker Compose setup maps the internal container port `8000` to random host ports, you'll first need to determine the dynamically assigned ports.

### Steps to Determine the Dynamic Port:

1. **Check the Dynamic Ports:**
   
   Run the following command to see the dynamic port mapping for your services:

   ```bash
   docker-compose ps
   ```

   You should see output similar to this:

   ```
   Name                          Command               State           Ports
   ---------------------------------------------------------------------------------
   fastapi-1         uvicorn main:app --host 0.0.0.0 --port 8000   Up      0.0.0.0:32768->8000/tcp
   fastapi-2         uvicorn main:app --host 0.0.0.0 --port 8000   Up      0.0.0.0:32769->8000/tcp
   fastapi-3         uvicorn main:app --host 0.0.0.0 --port 8000   Up      0.0.0.0:32770->8000/tcp
   ```

   Here, the `fastapi-1`, `fastapi-2`, and `fastapi-3` containers are exposed on the host machine with the following ports:

   - `fastapi-1` is mapped to `32768`
   - `fastapi-2` is mapped to `32769`
   - `fastapi-3` is mapped to `32770`

2. **Send `curl` Requests:**
   
   Now that you know the dynamically assigned host ports, you can send `curl` requests to each of the FastAPI replicas. Here's an example for each:

   - For `fastapi-1`:
     ```bash
     curl http://localhost:32768
     ```
   
   - For `fastapi-2`:
     ```bash
     curl http://localhost:32769
     ```
   
   - For `fastapi-3`:
     ```bash
     curl http://localhost:32770
     ```

   Each of these requests will return a response from the corresponding FastAPI instance.

### Example of Response:

Since you have the following endpoint in your FastAPI app:

```python
@app.get("/")
def read_root():
    server_name = socket.gethostname()  # Get the server/instance ID
    return {"message": f"Hello, from server {server_name}!"}
```

The `curl` command should return a response like this:

```json
{"message": "Hello, from server <hostname>!"}
```

Where `<hostname>` is the name of the server instance inside the container, which will be unique for each container (e.g., `fastapi-1`, `fastapi-2`, `fastapi-3`).

Let me know if you need further help!
