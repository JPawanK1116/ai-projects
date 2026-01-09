import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

smooth_x, smooth_y = 0, 0
prev_x, prev_y = 0, 0
smoothening = 7

def get_distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

def get_finger_positions(hand_landmarks, w, h):
    # Get coordinates of fingertips
    index_tip = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
    middle_tip = int(hand_landmarks.landmark[12].x * w), int(hand_landmarks.landmark[12].y * h)
    thumb_tip = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)
    return index_tip, middle_tip, thumb_tip

def fingers_up(hand_landmarks):
    fingers = []
    # Tip IDs: 8 (index), 12 (middle), 16 (ring), 20 (pinky)
    tip_ids = [8, 12, 16, 20]
    for tip_id in tip_ids:
        tip_y = hand_landmarks.landmark[tip_id].y
        lower_y = hand_landmarks.landmark[tip_id - 2].y
        fingers.append(tip_y < lower_y)
    return fingers  # [index, middle, ring, pinky]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_tip, middle_tip, thumb_tip = get_finger_positions(hand_landmarks, w, h)
            finger_states = fingers_up(hand_landmarks)

            # Mouse movement
            if finger_states[0] and not finger_states[1]:  # Only index finger up
                screen_x = np.interp(index_tip[0], (0, w), (0, screen_w))
                screen_y = np.interp(index_tip[1], (0, h), (0, screen_h))
                smooth_x = prev_x + (screen_x - prev_x) / smoothening
                smooth_y = prev_y + (screen_y - prev_y) / smoothening
                pyautogui.moveTo(smooth_x, smooth_y)
                prev_x, prev_y = smooth_x, smooth_y

            # Left click (Index + Thumb pinch)
            if get_distance(index_tip, thumb_tip) < 40:
                pyautogui.click()
                cv2.circle(frame, index_tip, 10, (0, 255, 0), cv2.FILLED)

            # Right click (Index + Middle pinch)
            if get_distance(index_tip, middle_tip) < 40:
                pyautogui.rightClick()
                cv2.circle(frame, middle_tip, 10, (0, 0, 255), cv2.FILLED)

            # Scroll (Index + Middle both up and far apart)
            if finger_states[0] and finger_states[1]:
                if abs(index_tip[1] - middle_tip[1]) < 30:  # aligned
                    if index_tip[1] < middle_tip[1] - 10:
                        pyautogui.scroll(30)
                    elif index_tip[1] > middle_tip[1] + 10:
                        pyautogui.scroll(-30)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Mouse Control", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
