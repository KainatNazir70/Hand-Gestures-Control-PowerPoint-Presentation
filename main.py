import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
# Keep max_num_hands=1 to prevent multi-hand conflicts, but we will read its classification
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Open Webcam
cap = cv2.VideoCapture(0)

# Gesture cooldown variables
cooldown_time = 1.2
last_gesture_time = 0

# Landmark IDs for the tips of the 5 fingers
tip_ids = [4, 8, 12, 16, 20]

print("System Active. Point:")
print("1 finger -> NEXT | 2 fingers -> PREVIOUS")
print("3 fingers -> START SLIDESHOW | 4 fingers -> EXIT SLIDESHOW | 5 fingers -> CLOSE POWERPOINT")
print("Press 'q' in the camera window to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a natural mirror view
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    total_fingers = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        # Loop through detected hand and its matching handedness classification
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            # Draw the hand skeleton overlay
            mp_draw.draw_landmarks(frame, hand_landmarks,
                                   mp_hands.HAND_CONNECTIONS)

            # Get Hand Label ('Left' or 'Right')
            # Note: Due to cv2.flip(), your physical Right hand is classified as 'Left' by MediaPipe
            hand_label = handedness.classification[0].label

            landmarks = hand_landmarks.landmark
            fingers = []

            # 1. Dynamic Thumb tracking logic
            if hand_label == "Left":  # Physical Right Hand (mirrored)
                if landmarks[tip_ids[0]].x > landmarks[tip_ids[0] - 1].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:  # Physical Left Hand (mirrored, hand_label == "Right")
                if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 2. Four Fingers tracking logic (remains the same for both hands)
            for id in range(1, 5):
                if landmarks[tip_ids[id]].y < landmarks[tip_ids[id] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Count total fingers raised
            total_fingers = fingers.count(1)

    # Trigger actions based on cooldown constraints
    current_time = time.time()
    if (current_time - last_gesture_time) > cooldown_time:
        if total_fingers == 1:
            pyautogui.press('right')
            print("➡️ Next Slide")
            last_gesture_time = current_time
        elif total_fingers == 2:
            pyautogui.press('left')
            print("⬅️ Previous Slide")
            last_gesture_time = current_time
        elif total_fingers == 3:
            pyautogui.press('f5')
            print("📺 Starting Slide Show (F5)")
            last_gesture_time = current_time
        elif total_fingers == 4:
            pyautogui.press('escape')
            print("❌ Exiting Slide Show (Esc)")
            last_gesture_time = current_time
        elif total_fingers == 5:
            pyautogui.hotkey('alt', 'f4')
            print("🚪 Closing Application (Alt + F4)")
            last_gesture_time = current_time

    # Display HUD status info on screen
    cv2.putText(frame, f'Fingers Tracked: {total_fingers}',
                (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the webcam window
    cv2.imshow("Presentation Control Feed", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
