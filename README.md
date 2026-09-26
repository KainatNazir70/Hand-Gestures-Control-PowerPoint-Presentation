# ✋ Hand Gesture Controlled PowerPoint 🎥

Control your PowerPoint presentation using hand gestures in real-time!

This project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to detect hand landmarks from a webcam, count raised fingers, and automate PowerPoint slide controls.

---

## 🚀 Features

* Real-time hand tracking using MediaPipe
* Finger counting logic
* Slide navigation using gestures
* Cooldown mechanism to prevent multiple triggers
* On-screen gesture status display
* Fully automated PowerPoint control
* Supports both **right and left hand**

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## ✋ Gesture Controls

| Fingers Shown | Action Performed |
| ------------- | ---------------- |
| ☝️ 1 Finger   | Next Slide       |
| ✌️ 2 Fingers  | Previous Slide   |
| 🤟 3 Fingers  | Start Slideshow  |
| 🖖 4 Fingers  | Exit Slideshow   |
| 🖐️ 5 Fingers | Close PowerPoint |

These gestures can be performed using either the **left or right hand**.

---

## ▶️ How to Run

Follow these steps to run the project:

### 1. Install the Required Libraries

Make sure Python is installed on your computer, then install the required dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

### 2. Place Your PowerPoint File

Put the PowerPoint presentation (`.pptx`) you want to control in the **same folder as `main.py`**.

Example:

```text
Hand-Gesture-PowerPoint/
│
├── main.py
├── presentation.pptx
└── README.md
```

### 3. Run `main.py`

Open a terminal in the project folder and run:

```bash
python main.py
```

### 4. Open Your PowerPoint

Open the PowerPoint presentation located in the **same folder as `main.py`**.

Keep the PowerPoint window available so the gesture controls can interact with it.

### 5. Control PowerPoint Using Gestures

Use your webcam and show the supported hand gestures.

The program will detect your fingers and automatically perform the corresponding PowerPoint action:

* ☝️ **1 Finger** → Next Slide
* ✌️ **2 Fingers** → Previous Slide
* 🤟 **3 Fingers** → Start Slideshow
* 🖖 **4 Fingers** → Exit Slideshow
* 🖐️ **5 Fingers** → Close PowerPoint

---

## ⚠️ Important Notes

* Make sure your **webcam is connected and accessible**.
* Keep your hand clearly visible to the webcam.
* Run `main.py` before using the gesture controls.
* Keep the PowerPoint presentation in the **same folder as `main.py`**.
* A short cooldown is used between gestures to prevent accidental repeated actions.
* Make sure PowerPoint is the active application when using the controls.

---

## 📁 Project Structure

```text
Hand-Gesture-PowerPoint/
│
├── main.py
├── presentation.pptx
└── README.md
```

---

## 🎯 Usage

1. Run `main.py`
2. Open the PowerPoint file from the same folder
3. Show your hand in front of the webcam
4. Use the gestures to control your presentation
5. Enjoy a hands-free PowerPoint presentation! 🎥✋
