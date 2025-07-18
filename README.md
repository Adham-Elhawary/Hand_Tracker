# ✋ Real-Time Hand Tracking and Finger Counter with OpenCV & MediaPipe

This project demonstrates real-time **hand tracking and finger counting** using **OpenCV** and **MediaPipe**. The application captures live video from your webcam, detects your hand, and counts how many fingers are up.

---

## 🧠 Features

- 🖐️ Real-time hand detection using **MediaPipe**
- 🧮 Automatic finger counting (thumb to pinky)
- 🔁 Live webcam input with OpenCV
- 🔵 Highlighting of the index fingertip
- 📊 Real-time finger count display

---
## 📸 Logic Overview

- **MediaPipe Hands**: Detects 21 hand landmarks per hand.
- **Finger Counting**: Compares fingertip positions with lower joints to determine if a finger is up.
- **Index Fingertip Detection**: The tip of the index finger (landmark `8`) is visually highlighted.

### 🧮 Counting Algorithm

- **Thumb**: Counted if it points to the right (x-coordinate of tip < x-coordinate of lower joint) — assuming right hand.
- **Other Fingers**: Counted if their tip’s y-coordinate is **above** (i.e., less than) the y-coordinate of the second joint below.

---

## 📷 Finger Landmark IDs

| Finger  | Tip ID |
|---------|--------|
| Thumb   | 4      |
| Index   | 8      |
| Middle  | 12     |
| Ring    | 16     |
| Pinky   | 20     |

---

## 💡 Example Use Cases

- ✋ Interactive gesture-controlled interfaces
- 🧏 Sign language recognition (starter logic)
- 🎓 Educational tools for learning computer vision and AI
  
---

## 🚀 Getting Started

### 📦 Requirements

Install Python dependencies:

 ```bash
 pip install opencv-python mediapipe

