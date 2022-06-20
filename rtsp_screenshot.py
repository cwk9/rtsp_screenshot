#!/usr/bin/env python3
#Grab an image from an RTSP Stream. Used to grab static image from escalator cameras to assist with sign setup. 
import cv2 #open-cv lib is needed for RTSP stream.
import os
import sys

def rtsp_screenshot():
    ipcams = ['192.168.4.190','192.168.4.204'] #list of hosts to grab data from.
    username = ''
    password = ''
    port = '554' #udp port number
    imagefiles = [] #array of files we've created. 
    combinedimagefile = 'combined3478dm38fgm4mnrs.jpg'

    for ipcam in ipcams:
        try:
            RTSP_URL = 'rtsp://' + username + ':' + password + '@' + ipcam + ':' + port

            os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
            
            cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
            
            if not cap.isOpened():
                print('Cannot open RTSP stream ' + ipcam)
                #exit(-1)
                pass

            filename = 'cam' + ipcam + '.jpg'
            imagefiles.append(filename)
            ret, frame = cap.read()
            cv2.imwrite(filename,frame)

            cap.release()
            cv2.destroyAllWindows()
        except:
            print("Unable to get data from camera. " + ipcam)

    #Combine to one image. 
    cv2images = []
    for imagefile in imagefiles:
        cv2images.append(cv2.imread(imagefile))
    im_v = cv2.vconcat(cv2images)
    cv2.imwrite(combinedimagefile, im_v)


