import socket
import json

print("SDN Path Tracing Client")

src = input("Enter Source Host: ")
dst = input("Enter Destination Host: ")

client = socket.socket()
client.connect(("localhost", 9999))

request = {
    "src": src,
    "dst": dst
}

client.send(json.dumps(request).encode())

response = client.recv(1024).decode()
path = json.loads(response)

print("\nForwarding Path:")
print(" → ".join(path))

client.close()