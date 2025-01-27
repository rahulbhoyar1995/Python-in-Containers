## Python in Container

#### 1. **Docker Installation and Setup**
   - **Check Docker version**:  
     ```
     docker --version
     ```
   - **Run Docker without sudo (Linux)**:  
     ```
     sudo usermod -aG docker $USER
     ```

#### 2. **Docker Images**
   - **List Docker images**:  
     ```
     docker images
     ```
   - **Pull an image from Docker Hub**:  
     ```
     docker pull <image_name>
     ```
   - **Build an image from a Dockerfile**:  
     ```
     docker build -t <image_name> .
     ```
   - **Remove a Docker image**:  
     ```
     docker rmi <image_name>
     ```

  - **Remove all Docker images**:  
     ```
     docker rmi $(docker images -q)
     ```
   - **Tag an image**:  
     ```
     docker tag <image_name> <new_image_name>:<tag>
     ```

#### 3. **Docker Containers**
   - **List running containers**:  
     ```
     docker ps
     ```
   - **List all containers (including stopped ones)**:  
     ```
     docker ps -a
     ```
   - **Run a container from an image**:  
     ```
     docker run <image_name>
     ```
   - **Run a container in the background (detached mode)**:  
     ```
     docker run -d <image_name>
     ```
   - **Run a container with a custom name**:  
     ```
     docker run --name <container_name> <image_name>
     ```
   - **Run a container with port mapping**:  
     ```
     docker run -p <host_port>:<container_port> <image_name>
     ```
   - **Stop a running container**:  
     ```
     docker stop <container_id>
     ```
   - **Stop running all containers**:  
     ```
     docker stop $(docker ps -aq)
     ```
   - **Removing all containers**:  
     ```
     docker rm $(docker ps -aq)
     ```
   - **Start a stopped container**:  
     ```
     docker start <container_id>
     ```
   - **Restart a container**:  
     ```
     docker restart <container_id>
     ```
   - **Remove a container**:  
     ```
     docker rm <container_id>
     ```
   - **Inspect container details**:  
     ```
     docker inspect <container_id>
     ```

#### 4. **Docker Volumes**
   - **List Docker volumes**:  
     ```
     docker volume ls
     ```
   - **Create a Docker volume**:  
     ```
     docker volume create <volume_name>
     ```
   - **Remove a Docker volume**:  
     ```
     docker volume rm <volume_name>
     ```
   - **Mount a volume to a container**:  
     ```
     docker run -v <volume_name>:<container_path> <image_name>
     ```

#### 5. **Docker Networks**
   - **List Docker networks**:  
     ```
     docker network ls
     ```
   - **Create a Docker network**:  
     ```
     docker network create <network_name>
     ```
   - **Connect a container to a network**:  
     ```
     docker network connect <network_name> <container_name>
     ```
   - **Disconnect a container from a network**:  
     ```
     docker network disconnect <network_name> <container_name>
     ```
   - **Remove a Docker network**:  
     ```
     docker network rm <network_name>
     ```

#### 6. **Docker Compose**
   - **Start services defined in `docker-compose.yml`**:  
     ```
     docker-compose up
     ```
   - **Start services in the background**:  
     ```
     docker-compose up -d
     ```
   - **Stop services**:  
     ```
     docker-compose down
     ```
   - **Build or rebuild services**:  
     ```
     docker-compose build
     ```
   - **View Compose logs**:  
     ```
     docker-compose logs
     ```

#### 7. **Docker System**
   - **Show Docker system information**:  
     ```
     docker info
     ```
   - **Remove all stopped containers, unused networks, images, and caches**:  
     ```
     docker system prune
     ```

These commands should help you get started with Docker and cover most of the basic operations you'll need to perform.
