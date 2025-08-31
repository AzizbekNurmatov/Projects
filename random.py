import cv2
import mediapipe as mp
import os

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Example: track index fingertip (landmark 8)
                x = int(hand_landmarks.landmark[8].x * frame.shape[1])
                y = int(hand_landmarks.landmark[8].y * frame.shape[0])

                cv2.circle(frame, (x, y), 10, (0,255,0), -1)

                # Simple trigger: if hand is far left of screen, open calculator
                if x < 100:  
                    os.system("calc")   # Windows example
                    print("Gesture detected → Opening Calculator")

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Gesture Control', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
