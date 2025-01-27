To keep your Docker containers running in the background and still be able to use the terminal for other tasks, you need to run `docker-compose` in detached mode.

Here’s how you can do that:

### 1. **Run Docker Compose in Detached Mode**

When you use the `docker-compose up` command, add the `-d` flag to run it in detached mode:

```bash
docker-compose up -d
```

This will start your containers in the background, and you can continue using your terminal for other tasks.

### 2. **Check the Running Containers**

If you want to check the status of the running containers, you can use:

```bash
docker-compose ps
```

This will show the status of all the containers running in your Docker Compose setup.

### 3. **Access Logs for Containers**

If you want to view the logs of any running container, you can use:

```bash
docker-compose logs fastapi-1
```

Replace `fastapi-1` with the container name for `fastapi-2` or `fastapi-3` if needed.

### 4. **Stop Containers When Done**

If you want to stop the containers after your work is done, you can use:

```bash
docker-compose down
```

This will stop and remove the containers, networks, and volumes created by Docker Compose.

### Summary of Commands:

- **Start containers in detached mode**:
  ```bash
  docker-compose up -d
  ```

- **View running containers**:
  ```bash
  docker-compose ps
  ```

- **View logs of a container**:
  ```bash
  docker-compose logs <container-name>
  ```

- **Stop and remove containers**:
  ```bash
  docker-compose down
  ```

This should keep your containers running in the background while you perform other tasks on your terminal.