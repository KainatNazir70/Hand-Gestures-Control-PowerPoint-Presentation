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

Follow these steps to run the project.

### 1. Clone or Download the Project

Download or clone this repository to your computer.

Open a terminal inside the project folder.

### 2. Install the Required Libraries

Make sure Python is installed on your computer, then install all required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Place Your PowerPoint File

Put the PowerPoint presentation (`.pptx`) you want to control in the **same folder as `main.py`**.

For example:

```text
Hand-Gesture-PowerPoint/
│
├── main.py
├── requirements.txt
├── presentation.pptx
└── README.md
```

### 4. Run `main.py`

Open a terminal in the project folder and run:

```bash
python main.py
```

### 5. Open Your PowerPoint

Open the PowerPoint presentation located in the **same folder as `main.py`**.

### 6. Control PowerPoint Using Gestures

Make sure your webcam is available and show your hand in front of the camera.

The program will detect your hand gestures and automatically control PowerPoint.

| Gesture       | Action           |
| ------------- | ---------------- |
| ☝️ 1 Finger   | Next Slide       |
| ✌️ 2 Fingers  | Previous Slide   |
| 🤟 3 Fingers  | Start Slideshow  |
| 🖖 4 Fingers  | Exit Slideshow   |
| 🖐️ 5 Fingers | Close PowerPoint |

---

## ⚠️ Important Notes

* Make sure your **webcam is connected and accessible**.
* Keep your hand clearly visible to the webcam.
* Run `main.py` before using the gesture controls.
* Keep the PowerPoint presentation in the **same folder as `main.py`**.
* Make sure PowerPoint is open when using the gesture controls.
* A cooldown mechanism is used to prevent accidental repeated actions.
* Gestures can be performed using either the **left or right hand**.
* Make sure the required Python dependencies are installed before running the program.

---

## 📁 Project Structure

```text
Hand-Gesture-PowerPoint/
│
├── main.py
├── requirements.txt
├── presentation.pptx
└── README.md
```

---

## 🎯 Usage

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Place your `.pptx` PowerPoint file in the same folder as `main.py`.

3. Run the program:

```bash
python main.py
```

4. Open your PowerPoint presentation.

5. Show your hand in front of the webcam.

6. Use the gestures to control your presentation.

Enjoy a **hands-free PowerPoint presentation!** 🎥✋

---

## 📌 Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Then open your PowerPoint file from the same folder and control it using hand gestures.
