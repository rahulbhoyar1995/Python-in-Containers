# Project 1 - With Kubernetes Tech Stack

When deploying **multiple FastAPI servers** behind a **load balancer**, the architecture ensures high availability, scalability, and fault tolerance. I'll guide you through creating a project where multiple FastAPI servers are deployed using **Docker** and managed with **Kubernetes**, demonstrating how requests are balanced across servers.

---

### Project Overview
- **App Functionality**: A FastAPI application serving "Hello, from server X!" (where X is the server instance ID).
- **Key Components**:
  1. **FastAPI**: API backend.
  2. **Docker**: To containerize the FastAPI app.
  3. **Kubernetes**: To deploy multi
  4. **Load Balancer**: To distribute traffic among instances.

---

### Steps and Code

#### 1. **Create the FastAPI App**
Create a file named `app.py`:

```python
from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    server_name = socket.gethostname()  # Get the server/instance ID
    return {"message": f"Hello, from server {server_name}!"}
```

---

#### 2. **Create a Requirements File**
Create `requirements.txt`:

```
fastapi
uvicorn
```

---

#### 3. **Create a Dockerfile**
Write the Dockerfile to containerize the FastAPI app:

```Dockerfile
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
```

---

#### 4. **Build the Docker Image**
Run the following command to build the Docker image:

```bash
docker build -t fastapi-multi-server .
```

---

#### 5. **Write Kubernetes Deployment and Service Files**

##### a. **Deployment YAML**
This creates multiple pods running the FastAPI app. Save it as `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
spec:
  replicas: 3  # Number of FastAPI instances
  selector:
    matchLabels:
      app: fastapi-app
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
      - name: fastapi-container
        image: fastapi-multi-server:latest  # Replace with your Docker Hub image if pushing
        ports:
        - containerPort: 8000
```

##### b. **Service YAML**
This exposes the pods via a load balancer. Save it as `service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  selector:
    app: fastapi-app
  ports:
    - protocol: TCP
      port: 80  # Port exposed to the outside world
      targetPort: 8000  # Internal FastAPI port
  type: LoadBalancer
```

---

#### 6. **Push Docker Image to a Registry**
Push the Docker image to a registry (like Docker Hub or AWS ECR):

```bash
docker tag fastapi-multi-server <your-dockerhub-username>/fastapi-multi-server
docker push <your-dockerhub-username>/fastapi-multi-server
```

---

#### 7. **Deploy to Kubernetes**
Make sure your Kubernetes cluster is running (e.g., using **Minikube** or a cloud provider).

Run the following commands:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

#### 8. **Access the App**
Use the command `kubectl get services` to get the external IP of the load balancer. Open the external IP in your browser or use `curl`:

```bash
curl http://<external-ip>
```

You’ll see responses like:

```json
{"message": "Hello, from server <instance-id>!"}
```

The `<instance-id>` changes as requests are distributed across multiple FastAPI instances.

---

### Explanation of Components

1. **FastAPI Application**:
   - A lightweight web framework.
   - Each instance responds with its unique hostname (server ID).

2. **Docker**:
   - Encapsulates the FastAPI app, making it portable and consistent.

3. **Kubernetes Deployment**:
   - Ensures multiple pods (instances) of the app are running.
   - Allows you to scale up/down by changing the `replicas` count.

4. **Kubernetes Service**:
   - Acts as a load balancer, distributing traffic among the pods.
   - `LoadBalancer` type makes the app accessible externally.

5. **Scaling**:
   - Increase or decrease replicas dynamically using:
     ```bash
     kubectl scale deployment fastapi-deployment --replicas=5
     ```

---

### Advantages of This Setup
- **Scalability**: Easily handle high traffic by increasing replicas.
- **Fault Tolerance**: If one pod fails, traffic is redirected to healthy pods.
- **Portability**: Docker and Kubernetes make the app deployable anywhere.

---

Let me know if you'd like more details on Kubernetes setup or pushing to Docker Hub!
