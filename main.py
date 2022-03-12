import asyncio
import time
import numpy as np
import cv2


def userTurn():
    cap = cv2.VideoCapture('http://192.168.1.119:4747/video')
    detector = cv2.QRCodeDetector()
    while cap.isOpened():
        frame = cap.read()
        print(frame)
        cv2.imshow('frame', frame)
        data = detector.detectAndDecode(frame)
        if data:
            print("QR Code detected-->", data)
            cap.release()
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


userTurn()
