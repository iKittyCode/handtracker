
import time
import mediapipe as mp
import cv2
import pyfirmata2
import math
PORT =  pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
ledPin = board.get_pin('d:5:p')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hand = mp_hands.Hands(max_num_hands=1)
while True:
    
    success, frame = cap.read() 
    if success:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(frame)
        if result.multi_hand_landmarks:
        
            
                for hand_landmarks in result.multi_hand_landmarks:
                    
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    handLandmarks = result.multi_hand_landmarks[0]
                    thumbTip = handLandmarks.landmark[4]
                    indexTip = handLandmarks.landmark[8]
                    distance = math.sqrt((thumbTip.x-indexTip.x)**2 +(thumbTip.y-indexTip.y)**2)
                    ledPin.write(distance)
                    time.sleep(0.1)
        cv2.imshow("capture image", frame) 
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()    
