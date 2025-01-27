from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    server_name = socket.gethostname()  # Get the server/instance ID
    return {"message": f"Hello, from server {server_name}!"}