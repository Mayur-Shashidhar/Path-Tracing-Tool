# ⚡ SDN Path Tracing Tool (Mininet-Based)

## 📌 Overview

This project implements a **Software Defined Networking (SDN) Path Tracing Tool** using a **Client–Server architecture**, enhanced with **real network emulation using Mininet**.

The tool traces the **path taken by packets** by:

* Reading **flow rules (logical simulation)**
* Reconstructing the **forwarding path hop-by-hop**
* Validating connectivity using a **real emulated network (ICMP over Open vSwitch)**

The system is fully **CLI-based** and consists of:

* 🖥️ One **client file**
* 🧠 One **server file**
* 🔌 Socket-based communication
* 🌐 Real network emulation using Mininet

---

## 🚀 What Makes This Project Strong

Unlike basic simulations, this project:

* ✅ Uses **Mininet + Open vSwitch (OVS)** for real network emulation
* ✅ Performs **actual packet forwarding validation (ICMP ping)**
* ✅ Runs switches in **standalone (learning) mode without a controller**
* ✅ Combines **SDN logic + real network execution**
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

### 5. Validate Using Real Network (Mininet + OVS)

Before tracing, the system validates connectivity using:

* ICMP ping between hosts (`h1 → h2`)
* Open vSwitch in **standalone mode** (L2 learning switch behavior)
* Ensures **actual packet delivery**, not just simulation

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
     │     └── OVS Switches (standalone mode)
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
* Switch Mode: **Standalone (learning switch)**
* No external controller required

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

```
H1 → H2
```

---

### 🔹 Step 2 — Server Processing

1. Initialize Mininet topology
2. Run `pingAll()` to establish connectivity
3. Validate using ICMP (`h1 → h2`)
4. Read flow rules (logical model)
5. Trace forwarding path
6. Detect errors (loop / missing rule)

---

### 🔹 Step 3 — Response

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
* Real packet validation using Mininet
* OVS standalone switching (no controller dependency)
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

It demonstrates how **packet forwarding decisions** can be analyzed and validated using **actual network behavior**, making it a strong foundation for advanced SDN systems.

---

## 🚀 Future Improvements

* 🔄 Replace static flow tables with real switch flow extraction (`ovs-ofctl`)
* 🌐 Add web-based visualization (graph view)
* ⚡ Integrate SDN controller (Ryu)
* 📊 Add latency and path metrics analysis
* 🔍 Support dynamic topologies
