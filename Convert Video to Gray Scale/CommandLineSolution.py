import cv2
import sys
import time

arguments = sys.argv
if len(arguments) != 2 : 
    print("Invalid Number of Arguments Provided")

else: 
    video = cv2.VideoCapture(arguments[1])
    start = time.time()


    while True: 
        ret, frame = video.read()
        if ret: 
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('temp',gray)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else : 
            break

    video.release()
    end = time.time()
    print("Time taken to convert to Gray Scale",end - start)
