import cv2 
import time
import numpy as np

#key = cv2. waitKey(1)

lower_range = np.array([0,100,100])
upper_range = np.array([5,255,255])


webcam = cv2.VideoCapture(0)
while True:
    print ("sleeping...")
    #time.sleep(1)
    try:
        check, frame = webcam.read()
        print ("Check")
        #print(check) #prints true as long as the webcam is running
        #print ("Frame")
        #print(frame) #prints matrix values of each framecd 
        #cv2.imshow("Capturing", frame)
        print ("Write")
	cv2.imwrite(filename='img.jpg', img=frame)
        #webcam.release()
        print ("Read")
	image = cv2.imread('img.jpg')
        print ("Color")
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        print ("mask")
	mask = cv2.inRange(hsv, lower_range, upper_range)
        print ("Show")
	cv2.imshow('image_window_name', image)
	cv2.imshow('mask_window_name', mask)
	cv2.waitKey(0)
	#time.sleep(1)
	cv2.destroyAllWindows()
  
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

webcam.release()
    
