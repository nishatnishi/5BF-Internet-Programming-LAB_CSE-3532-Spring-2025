# 📌 Project Title: Real-Time Human Pose Detection

## 🛠️ Technologies Used

- **Python** – Programming language used for the main logic.
- **MediaPipe** – A Google library for real-time pose estimation and other ML-based computer vision tasks.
- **OpenCV** – For accessing the laptop camera, processing video frames, and displaying output.
- **NumPy** – Used for handling image array manipulations.

---

## 💻 Hardware Used

- **Laptop Camera** – Built-in webcam used to capture live video stream.

---

## 🧰 Software Tools

- **Visual Studio Code** – Python code editor.

---

## ⚙️ How It Works

1. Live camera feed is captured using OpenCV (`cv2.VideoCapture`).
2. Each frame is converted from BGR to RGB (because MediaPipe requires RGB input).
3. The frame is sent to MediaPipe’s pose model to detect body landmarks (e.g., shoulders, elbows, knees).
4. If a human pose is detected, MediaPipe returns 33 key points with x, y, z coordinates.
5. Using MediaPipe’s drawing utilities, the program draws a skeleton over the person in real time.
6. The annotated frame is displayed using `cv2.imshow()` and updates continuously.

---

## 🌟 Main Features

- Real-time detection with very low delay.
- Visual representation of human body posture.
- Works directly on a laptop with no extra hardware.

---

## 👥 Team Responsibilities

### 👤 Team Member 1: `C213214R`

Responsible for the initial setup and implementation of the core real-time pose detection system:

- Configured and accessed the laptop camera using OpenCV.
- Integrated the MediaPipe Pose model to detect human body landmarks.
- Captured live video frames and successfully rendered pose landmarks and skeletal connections on each frame.
- Ensured smooth and real-time video display with accurate visual tracking.

> This forms the foundational layer of the project upon which further motion analysis features will be built.

---

### 👤 Team Member 2: `C213213R`

Responsible for the upcoming analytical components of the project:

- Will identify and extract key joint coordinates from the MediaPipe pose landmarks.
- Will apply trigonometric functions to calculate angles between joints (e.g., elbow, knee).
- Will implement logic to track and count body movements such as bicep curls and evaluate posture quality.

> This module is under development and will integrate seamlessly with the current real-time system in the next phase.
