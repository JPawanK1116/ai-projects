# Smart Traffic Light System

## 📌 Project Overview
An intelligent traffic management system capable of optimizing signal timings based on real-time vehicle density detection from live footage or images.

## 🎯 Objectives
- To reduce traffic congestion using AI.
- To detect vehicles accurately in varied lighting conditions.
- To dynamically adjust traffic light timers.

## 🧠 Concepts & Tech Stack
- **Computer Vision:** Object Detection (YOLO / OpenCV)
- **Image Processing:** Vehicle Counting, Density Estimation
- **Libraries:** OpenCV, Python, Pygame (for simulation)

## 🏗️ Structure
- **src/simulation.py:** Main script running the traffic simulation.
- **data/images:** Sample images used for testing the detection logic.

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the simulation:
    ```bash
    python src/simulation.py
    ```

## 🔮 Future Improvements
- Implement Deep Learning based detection (YOLOv8) for higher accuracy.
- Connect to real-world traffic camera feeds.
