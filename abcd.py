import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    try:
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
    except Exception as es :
        pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()