import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
##import pyfirmata
import pyfirmata2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

minHand, maxHand = 20, 250
minBar, maxBar = 400, 150
minAngle, maxAngle = 0, 120

port = "COM6"
board = pyfirmata2.Arduino(port)
servoPin = board.get_pin('d:5:s') # pin 5 Arduino

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        thumbTip = hands[0]["lmList"][4]
        indexTip = hands[0]["lmList"][8]

        # Calculate the distance between thumbTip and indexTip manually
        length = math.hypot(indexTip[0] - thumbTip[0], indexTip[1] - thumbTip[1])

        servoVal = np.interp(length, [minHand, maxHand], [minAngle, maxAngle])
        # Display length and bar on the image
        cv2.rectangle(img, (100, 100), (360, 30), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'Length: {int(length)}', (130, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 3)

        ##cv2.putText(img, f'Servo: {int(servoVal)}', (130, 110), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 3)

        bar = np.interp(length, [minHand, maxHand], [minBar, maxBar])
        cv2.rectangle(img, (1180, 150), (1215, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (1180, int(bar)), (1215, 400), (0, 255, 0), cv2.FILLED)

        servoPin.write(servoVal)

    cv2.imshow("PPP", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()