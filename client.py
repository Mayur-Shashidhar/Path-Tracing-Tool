import socket
import json

print("SDN Path Tracing Client")

src = input("Enter Source Host (H1/H2): ").strip().upper()
dst = input("Enter Destination Host (H1/H2): ").strip().upper()

client = socket.socket()

try:
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

except ConnectionRefusedError:
    print("Server not running. Start server first.")

finally:
    client.close()
