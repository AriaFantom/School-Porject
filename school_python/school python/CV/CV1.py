import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(1)
mpHands = mp.sol.Hands
hands = mpHands.Hands()

while true:
    success, img=cap.read()
    cv2.imshow("Image" , img)
    cv.waitKey(1)