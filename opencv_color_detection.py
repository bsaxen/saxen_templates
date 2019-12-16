import numpy as np
import cv2

#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print (flags)
#exit()

R_lower_range    = np.array([0,100,100])
R_upper_range    = np.array([0,255,255])
#R_lower_range    = np.array([160,20,70])
#R_upper_range    = np.array([190,255,255])

#B_lower_range    = np.array([100,100,0])
#B_upper_range    = np.array([255,255,0])
B_lower_range    = np.array([101,50,38])
B_upper_range    = np.array([110,255,255])

G_lower_range    = np.array([36,0,0])
G_upper_range    = np.array([86,255,255])


Y_lower_range    = np.array([15,0,0])
Y_upper_range    = np.array([36,255,255])


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
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #hsv = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2BGR)
    cv2.imshow('HSV', hsv)

    x1 = 250
    y1 = 400
    x2 = 270
    y2 = 420
    # Red
    mask = cv2.inRange(hsv, R_lower_range, R_upper_range)
    cv2.imshow('Red', mask)
    pixel = mask[x1:y1,x2:y2]
    #pixel = mask[x1,y1]
    print "red "
    print (pixel)
    # Green
    mask = cv2.inRange(hsv, G_lower_range, G_upper_range)
    cv2.imshow('Green', mask)
    pixel = mask[x1:y1,x2:y2]
    #pixel = mask[x1,y1]
    print "green "
    print (pixel)
    # Blue
    mask = cv2.inRange(hsv, B_lower_range, B_upper_range)
    cv2.imshow('Blue', mask)
    pixel = mask[x1:y1,x2:y2]
    #pixel = mask[x1,y1]
    print "blue "
    print (pixel)
    # Yellow
    mask = cv2.inRange(hsv, Y_lower_range, Y_upper_range)
    cv2.imshow('yellow', mask)
    pixel = mask[x1:y1,x2:y2]
    #pixel = mask[x1,y1]
    print "yellow "
    print (pixel)

    key = cv2.waitKey(100)
    #print ("waitkey " + str(key))
    #print (str(ord('q')))
    #if key & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
