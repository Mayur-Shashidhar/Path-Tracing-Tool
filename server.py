import socket
import json
import os

from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.topo import Topo


class SDNTopology(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        
        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')

        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, h2)



def start_network():
    print("🧹 Cleaning previous Mininet state...")
    os.system("mn -c")

    topo = SDNTopology()

    net = Mininet(
        topo=topo,
        controller=None,   
        switch=OVSSwitch,
        link=TCLink,
        autoSetMacs=True   
    )

    net.start()

    print("Initializing network (pingAll)...")
    net.pingAll()

    print("Mininet network started (standalone mode)")
    return net



topology = {
    "S1": {"1": "H1", "2": "S2"},
    "S2": {"1": "S1", "2": "S3"},
    "S3": {"1": "S2", "2": "H2"}
}

host_to_switch = {
    "H1": "S1",
    "H2": "S3"
}

flows = {
    "S1": {"H2": 2},
    "S2": {"H2": 2},
    "S3": {"H2": 2}
}



def validate_with_mininet(net):
    print("\nValidating using Mininet (ping)...")

    h1 = net.get('h1')
    h2 = net.get('h2')

    result = h1.cmd('ping -c 1 ' + h2.IP())
    print(result.strip())

    return "0% packet loss" in result



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



def main():
    net = start_network()

    server = socket.socket()
    server.bind(("localhost", 9999))
    server.listen(5)

    print("\nSDN Path Tracing Server Running with Mininet...\n")

    try:
        while True:
            client, addr = server.accept()

            data = client.recv(1024).decode()
            req = json.loads(data)

            src = req.get("src")
            dst = req.get("dst")

            if src not in host_to_switch or dst not in host_to_switch:
                path = ["Invalid hosts"]
            else:
                if not validate_with_mininet(net):
                    path = ["Path not found"]
                else:
                    path = trace_path(src, dst)

            client.send(json.dumps(path).encode())
            client.close()

    except KeyboardInterrupt:
        print("\nShutting down server...")
        net.stop()
        os.system("mn -c")
        server.close()


if __name__ == "__main__":
    main()
