# ⚡ SDN Path Tracing Tool (Mininet-Based)

## 📌 Overview

This project implements a **Software Defined Networking (SDN) Path Tracing Tool** using a **Client–Server architecture**, enhanced with **real network emulation using Mininet**.

The tool traces the **path taken by packets** by:

* Reading **flow rules (logical simulation)**
* Reconstructing the **forwarding path hop-by-hop**
* Validating connectivity using a **real emulated network**

The system is fully **CLI-based** and consists of:

* 🖥️ One **client file**
* 🧠 One **server file**
* 🔌 Socket-based communication
* 🌐 Real network emulation using Mininet

---

## 🚀 What Makes This Project Strong

Unlike basic simulations, this project:

* ✅ Uses **Mininet** to emulate a real network
* ✅ Validates packet delivery using **ICMP (ping)**
* ✅ Combines **theoretical SDN logic + practical network execution**
* ✅ Implements a **client–server distributed system**

---

## 🎯 Objectives

The tool satisfies the following requirements:

### 1. Identify and Display Packet Path

The server reconstructs the full forwarding path and sends it to the client.

---

### 2. Track Flow Rules

The system logs each forwarding decision:

```
S1 → port 2
S2 → port 2
S3 → port 2
```

---

### 3. Identify Forwarding Path

The tracer follows output ports across switches until the destination is reached.

---

### 4. Display Route

The client prints the complete route:

```
H1 → S1 → S2 → S3 → H2
```

---

### 5. Validate Using Real Network (Mininet)

Before tracing, the system validates connectivity using:

* ICMP ping between hosts
* Ensures the path is actually reachable

---

## 🏗️ Architecture

```
Client (CLI)
     │
     │  Request (src, dst)
     ▼
Server (Path Tracing Engine)
     │
     ├── Mininet Network (Real Emulation)
     ├── SDN Topology (Logical Model)
     ├── Flow Tables
     └── Path Tracer
     │
     ▼
Response (Forwarding Path)
```

---

## 📁 Project Structure

```
SDN-Path-Tracer/
│
├── client.py
└── server.py
```

---

## 🌐 Network Topology (Mininet)

```
H1 ── S1 ── S2 ── S3 ── H2
```

* Hosts: `H1`, `H2`
* Switches: `S1`, `S2`, `S3`
* Links: Linear chain topology

---

## 📊 Flow Table (Logical Model)

| Switch | Destination | Output Port |
| ------ | ----------- | ----------- |
| S1     | H2          | 2           |
| S2     | H2          | 2           |
| S3     | H2          | 2           |

---

## 🧠 Path Tracing Algorithm

1. Start from source host's switch
2. Read matching flow rule
3. Extract output port
4. Move to next node
5. Repeat until destination
6. Detect loops if revisited
7. Return full path

---

## ⚙️ How It Works

### 🔹 Step 1 — Client Request

User enters:

```
H1 → H2
```

---

### 🔹 Step 2 — Server Processing

1. Validate using Mininet (ping)
2. Read flow rules
3. Trace forwarding path
4. Detect errors (loop / missing rule)

---

### 🔹 Step 3 — Response

Client receives and displays:

```
H1 → S1 → S2 → S3 → H2
```

---

## ▶️ How to Run

### ✅ Prerequisites

* Python 3
* Mininet installed

---

### Step 1 — Start Server (IMPORTANT)

```bash
sudo python3 server.py
```

---

### Step 2 — Run Client

```bash
python3 client.py
```

---

## 🧪 Example Execution

### Client Input

```
Enter Source Host: H1
Enter Destination Host: H2
```

---

### Server Output

```
Validating using Mininet (ping)...
0% packet loss

Tracking Flow Rules...
S1 → port 2
S2 → port 2
S3 → port 2
```

---

### Client Output

```
Forwarding Path:
H1 → S1 → S2 → S3 → H2
```

---

## ✅ Validation Tests

### ✔ Test Case 1 — Valid Path

```
Input:  H1 → H2
Output: H1 → S1 → S2 → S3 → H2
```

---

### ❌ Test Case 2 — Invalid Destination

```
Input:  H1 → H3
Output: Path not found
```

---

### 🔁 Test Case 3 — Loop Detection

```
Output: Loop detected
```

---

## ✔ Features

* Client–Server architecture
* CLI-based interface
* SDN path tracing logic
* Flow rule tracking
* Forwarding path reconstruction
* Loop detection
* Real network validation using Mininet
* Lightweight and modular design

---

## 🛠️ Technologies Used

* Python
* Socket Programming
* JSON
* Mininet (Network Emulation)
* Open vSwitch (OVS)

---

## 📌 Sample Output

```
Tracing Path: H1 → H2

Validating using Mininet (ping)...
0% packet loss

Tracking Flow Rules...
S1 → port 2
S2 → port 2
S3 → port 2

Final Path:
H1 → S1 → S2 → S3 → H2
```

---

## 📖 Conclusion

This project implements a **hybrid SDN Path Tracing Tool** that combines:

* 📊 Logical flow-based path computation
* 🌐 Real network emulation using Mininet

It demonstrates how **packet forwarding decisions** can be analyzed, validated, and visualized in a controlled SDN environment, making it a strong foundation for advanced networking and SDN-based systems.

---

## 🚀 Future Improvements

* 🔄 Replace static flow tables with real switch flow extraction (`ovs-ofctl`)
* 🌐 Add web-based visualization (graph view)
* ⚡ Integrate SDN controller (Ryu)
* 📊 Add latency and path metrics analysis
* 🔍 Support dynamic topologies

---
