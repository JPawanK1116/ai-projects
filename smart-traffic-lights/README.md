# Smart Traffic Light System

## 📌 Project Overview
The Smart Traffic Light System is an AI-based traffic management solution designed to optimize traffic signal timings using vehicle density analysis.  
This project contains **two working approaches**:
1. A **traffic signal simulator** that demonstrates real-time signal behavior using mathematical traffic formulas.
2. A **real-time vehicle detection system** that analyzes CCTV or live traffic footage using Computer Vision.

Together, these approaches show both **theoretical logic** and **real-world applicability** of intelligent traffic control systems.

---

## 🎯 Project Objectives
- Reduce traffic congestion using intelligent signal control.
- Demonstrate real-time traffic signal behavior through simulation.
- Detect and count vehicles from CCTV or live video feeds.
- Dynamically adjust signal timings based on traffic density.

---

## 🧠 Concepts & Technologies Used
- **Computer Vision:** Vehicle Detection & Counting
- **Image Processing:** Frame analysis, object tracking
- **Traffic Algorithms:** Density-based signal timing logic
- **Simulation Systems:** Real-time signal visualization

### Tech Stack
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy, Pygame
- **Input Sources:** Images, recorded CCTV footage, live video streams

---

## 🏗️ Project Structure

```
smart-traffic-light-system/
│
├── src/
│ ├── simulation.py        # Traffic signal simulator using traffic formulas
│ └── vehicle_detection.py # Real-time vehicle detection from video/CCTV
│
├── data/
│ ├── images/              # Sample images for testing
│ └── videos/              # CCTV or traffic footage samples
│
├── requirements.txt
└── README.md
```

---

## 🚦 System Modes

### 1️⃣ Traffic Signal Simulator
- Simulates traffic signals in real time.
- Uses predefined traffic density formulas.
- Helps visualize how signal timings change based on vehicle flow.
- Useful for understanding **traffic logic without real footage**.

### 2️⃣ Real-Time Vehicle Detection (Added Feature)
- Detects vehicles from CCTV or live camera footage.
- Counts vehicles lane-wise using Computer Vision.
- Outputs traffic density data that can be used for dynamic signal control.
- Demonstrates **real-world intelligent traffic systems**.

---

## 🚀 How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Traffic Simulation
```bash
python src/simulation.py
```

### Step 3: Run Real-Time Vehicle Detection
```bash
python src/vehicle_detection.py
```

## 📊 Key Observations
- Density-based signal timing can significantly reduce idle waiting time.
- Simulation helps validate traffic control logic before real deployment.
- Computer Vision enables scalable, camera-based traffic monitoring.

## 🔮 Future Enhancements
- Integrate deep learning models (YOLOv8) for higher accuracy.
- Combine simulation logic with live detection for fully automated signals.
- Deploy on edge devices for real-time city-scale implementation.
- Add dashboard for traffic analytics and visualization.

## 📌 Conclusion
This project demonstrates both simulation-based traffic control and real-time AI-driven vehicle detection, making it a strong foundation for smart city and intelligent transportation systems.
