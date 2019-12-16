import numpy as np
import cv2

R_lower_range    = np.array([0,100,100])
R_upper_range    = np.array([0,255,255])

Y_lower_range    = np.array([0,0,100])
Y_upper_range    = np.array([0,0,255])

B_lower_range    = np.array([100,100,0])
B_upper_range    = np.array([255,255,0])

G_lower_range    = np.array([100,0,100])
G_upper_range    = np.array([255,0,255])

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    #cv2.imshow('frame',frame)

    cv2.imwrite(filename='img.jpg', img=frame)
    image = cv2.imread('img.jpg')
    cv2.imshow('image',image)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Red
    mask = cv2.inRange(hsv, R_lower_range, R_upper_range)
    cv2.imshow('Red', mask)
    # Green
    mask = cv2.inRange(hsv, G_lower_range, G_upper_range)
    cv2.imshow('Green', mask)
    # Blue
    mask = cv2.inRange(hsv, B_lower_range, B_upper_range)
    cv2.imshow('Blue', mask)
    # Yellow
    mask = cv2.inRange(hsv, Y_lower_range, Y_upper_range)
    cv2.imshow('yellow', mask)

    key = cv2.waitKey(10)
    #print ("waitkey " + str(key))
    #print (str(ord('q')))
    #if key & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
