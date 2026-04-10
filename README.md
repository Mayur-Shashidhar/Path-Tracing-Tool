# Path Tracing Tool (SDN-Based)

## 📌 Overview

This project implements a **Software Defined Networking (SDN) Path Tracing Tool** using a **Client–Server architecture**.
The tool traces the **path taken by packets** by reading **flow rules** from switches and reconstructing the **forwarding path** hop-by-hop.

The implementation is fully **CLI-based** and uses:

* One **client file**
* One **server file**
* Socket-based communication

---

## 🎯 Objectives

The tool satisfies the following requirements:

**1. Identify and display the path taken by packets** : 
The server traces packet movement switch-by-switch using SDN flow rules and returns the full path, which is displayed by the client.

**2. Track flow rules** :
During tracing, the server reads flow table entries and prints the matched rule (switch → output port) used for forwarding.

**3. Identify forwarding path** :
The tracing engine follows output ports from one switch to the next until the destination host is reached.

**4. Display route** :
The client prints the final route in ordered format (e.g., `H1 → S1 → S2 → S3 → H2`).

**5. Validate using tests** :
Different source–destination inputs are executed to verify valid paths, missing flow rules, and loop detection.

---

## 🏗️ Client–Server Architecture

```
Client (CLI)
     │
     │  Request (src, dst)
     ▼
Server (Path Tracing Engine)
     │
     ├── SDN Topology
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

## ⚙️ Server Responsibilities

The server performs:

* Maintain SDN topology
* Store switch flow tables
* Track flow rules
* Identify forwarding path
* Detect loops
* Return final route

---

## 💻 Client Responsibilities

The client performs:

* Takes source host input
* Takes destination host input
* Sends request to server
* Receives traced path
* Displays final route

---

## 🔎 SDN Topology Used

```
H1 ── S1 ── S2 ── S3 ── H2
```

---

## 📊 Flow Table

| Switch | Destination | Output Port |
| ------ | ----------- | ----------- |
| S1     | H2          | 2           |
| S2     | H2          | 2           |
| S3     | H2          | 2           |

---

## 🧠 Path Tracing Algorithm

1. Start from source host switch
2. Read matching flow rule
3. Get output port
4. Move to next switch
5. Repeat until destination
6. Return full path

---

## ▶️ How to Run

### Step 1 — Start Server

Open Terminal 1:

```
python server.py
```

Output:

```
SDN Path Tracing Server Running...
```

---

### Step 2 — Run Client

Open Terminal 2:

```
python client.py
```

---

## 🧪 Example Execution

### Client Input

```
SDN Path Tracing Client
Enter Source Host: H1
Enter Destination Host: H2
```

---

### Server Output (Tracking Flow Rules)

```
Tracking Flow Rules...
S1 → port 2
S2 → port 2
S3 → port 2
```

---

### Client Output (Final Route)

```
Forwarding Path:
H1 → S1 → S2 → S3 → H2
```

---

## 🔁 Working Flow

1. Client sends source and destination
2. Server receives request
3. Server reads flow rules
4. Server follows forwarding path
5. Server constructs route
6. Server returns path
7. Client displays route

---

## ✅ Validation Tests

### Test Case 1 — Valid Path

Input:

```
H1 → H2
```

Output:

```
H1 → S1 → S2 → S3 → H2
```

---

### Test Case 2 — Path Not Found

Input:

```
H1 → H3
```

Output:

```
Path not found
```

---

### Test Case 3 — Loop Detection

If switches form a loop:

```
Loop detected
```

---

## ✔ Features

* Client–Server architecture
* CLI-based interface
* SDN path tracing
* Flow rule tracking
* Forwarding path identification
* Route display
* Validation tests
* Loop detection
* Minimal implementation

---

## 🛠️ Technologies Used

* Python
* Socket Programming
* JSON
* CLI

---

## 📌 Sample Final Output

```
Tracing Path: H1 → H2

Tracking Flow Rules...
S1 → port 2
S2 → port 2
S3 → port 2

Final Path:
H1 → S1 → S2 → S3 → H2
```

---

## 📖 Conclusion

This project implements a **Client–Server based SDN Path Tracing Tool** that tracks **flow rules**, identifies the **forwarding path**, and displays the **route taken by packets**. The tool satisfies all specified requirements using a simple CLI-based implementation.
