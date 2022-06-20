#!/usr/bin/env python3
#Grab an image from an RTSP Stream. 
#Returns cv2 image as numpy.ndarray. Can be written file using opencv.
#Example
#newimage = rtsp_screenshot(ipcam = '192.168.1.123', username = 'admin', password = 'yourpw', port = '554')
#cv2.imwrite('testimg.jpg',newimage)
import cv2 #open-cv lib is needed for RTSP stream.
import os
import sys
from copy import deepcopy

def rtsp_screenshot(ipcam = '', username = '', password = '', port = '554'):
#    ipcam = '' #list of hosts to grab data from.
#    username = ''
#    password = ''
#    port = '554' #udp port number

    try:
        if username != '' or password != '': 
            RTSP_URL = 'rtsp://' + username + ':' + password + '@' + ipcam + ':' + port
        else: #No auth
            RTSP_URL = 'rtsp://' + ipcam + ':' + port

        os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
        
        cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
        
        if not cap.isOpened():
            return('Cannot open RTSP stream ' + ipcam)
            exit(-1)
            pass
        else:
            ret, frame = cap.read()
            returnimage = deepcopy(frame) #copy pic before clean up

            #Clean up our CV2 data
            cap.release()
            cv2.destroyAllWindows()

    except:
        return("Unable to get data from camera. " + ipcam)

    return(returnimage)

