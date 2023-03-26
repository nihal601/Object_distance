import numpy as np
import cv2
from cv2 import aruco

import time

cap = cv2.VideoCapture("/home/nihal/Downloads/forklift.mp4")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

# inputsource = "gst-launch-1.0 uridecodebin uri=http://172.16.16.59:8080/video ! nvvideoconvert ! videorate ! video/x-raw,format=(string)I420,width=(int)1980,height=(int)1080,framerate=10/1 ! videoconvert ! appsink sync=false"

#cap = cv2.VideoCapture("/home/raman/Downloads/ar.mp4")
while 1:
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()

    # frame = cv2.imread("/home/nihal/Documents/Mondelez_vie/forklift/5.jpg")
    if not ret:
        print("No camera feed")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(corners)
    for cor in corners:
        #print(cor)
        width_pixel = cor[0][0][0] - cor[0][1][0]
        dist = (17 * 1584) / width_pixel
        print(dist)
        frame = cv2.putText(frame, 'Distance in Meters: {:.2f}'.format(dist/100), (100 , 100), 
                cv2.FONT_HERSHEY_COMPLEX, 2.7, (0, 0, 255), 2, cv2.LINE_AA)
        
    print("==="*20)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    time.sleep(0.1)
    cv2.namedWindow("Aruco", cv2.WINDOW_NORMAL)
    cv2.imshow("Aruco", frame_markers)
    result.write(frame_markers)
    cv2.waitKey(1) 
    
cap.release()
result.release()