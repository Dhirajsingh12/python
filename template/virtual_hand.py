import cv2
import mediapipe as mp
import pyautogui
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

prev_action = None

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)  
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = hand_landmarks.landmark
            finger_tip_y = landmarks[8].y  
            thumb_tip_y = landmarks[4].y  
            wrist_y = landmarks[0].y       
            finger_tip_x = landmarks[8].x  

            if wrist_y < 0.3 and prev_action != "play_pause":
                pyautogui.press('space')
                print("Play/Pause toggled")
                prev_action = "play_pause"

            elif finger_tip_x < 0.2 and prev_action != "previous":
                pyautogui.press('left')
                print("Previous Video / Rewind")
                prev_action = "previous"

            elif finger_tip_x > 0.8 and prev_action != "next":
                pyautogui.press('right')
                print("Next Video / Forward")
                prev_action = "next"

            elif thumb_tip_y < finger_tip_y and prev_action != "like":
                pyautogui.press('l') 
                print("Liked Video!")
                prev_action = "like"
            else:
                pass 

    else:
        prev_action = None  

    cv2.imshow("YouTube Controller", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
