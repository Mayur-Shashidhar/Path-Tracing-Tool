import socket
import json

#Topology
topology = {
    "S1": {"1": "H1", "2": "S2"},
    "S2": {"1": "S1", "2": "S3"},
    "S3": {"1": "S2", "2": "H2"}
}

#Host Mapping
host_to_switch = {
    "H1": "S1",
    "H2": "S3"
}

#Flow Table
flows = {
    "S1": {"H2": 2},
    "S2": {"H2": 2},
    "S3": {"H2": 2}
}


def trace_path(src, dst):
    print("\nTracking Flow Rules...")

    current = host_to_switch[src]
    path = [src, current]

    visited = set()

    while True:

        if current in visited:
            return ["Loop detected"]
        visited.add(current)

        if dst not in flows[current]:
            return ["Path not found"]

        out_port = flows[current][dst]

        print(f"{current} → port {out_port}")

        next_node = topology[current][str(out_port)]
        path.append(next_node)

        if next_node == dst:
            break

        current = next_node

    return path


#Server Setup
server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("SDN Path Tracing Server Running...")

while True:
    client, addr = server.accept()

    data = client.recv(1024).decode()
    req = json.loads(data)

    src = req["src"]
    dst = req["dst"]

    path = trace_path(src, dst)

    client.send(json.dumps(path).encode())
    client.close()