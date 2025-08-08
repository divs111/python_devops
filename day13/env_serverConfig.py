import os

server = os.getenv("SERVER_NAME" , "localhost")
port = os.getenv("SERVER_PORT" , "8080")

print(f"Connecting to server : {server} on port: {port}")

