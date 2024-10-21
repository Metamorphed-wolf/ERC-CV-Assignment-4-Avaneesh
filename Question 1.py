import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands#to detect hands
mp_drawing = mp.solutions.drawing_utils #to draw the detected hands
cap = cv2.VideoCapture(0) #to start the webcam
with mp_hands.Hands(
    max_num_hands=2, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()  # to read frame from webcam
        if not ret:
            break
        
        
        frame = cv2.flip(frame, 1) # to flip the frame for mirror effect
        
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)# to convert the frame to RGB
        
        
        results = hands.process(rgb_frame) 
        
       
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        
        cv2.imshow('Hand Contours', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #breaks the loop if q is pressed
            break


cap.release()
cv2.destroyAllWindows() # to release the webcam and close the windows


