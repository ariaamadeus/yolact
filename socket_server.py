import socket
import sys
import os

import cv2
import numpy as np

import struct

#HOST = '192.168.5.71'
#PORT = 7002       # Arbitrary non-privileged port
s = None
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
CHANNEL=3

conn = 0

def socketToNumpy(cameraFeed, sockData):
    k=3
    j=cameraFeed.shape[1]
    i=cameraFeed.shape[0]
    sockData = np.fromstring(sockData, np.uint8)
    cameraFeed = np.tile(sockData, 1).reshape((i,j,k))

    return cameraFeed
def startServer(HOST,PORT):
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print ('could not open socket')
        sys.exit(1)
    return s

def recvData(s):
    global conn
    
    print('Waiting Connection...')
    conn, addr = s.accept()
    print ('Connected by', addr)

    running = True
    while running:
        i, ptr = (0,0)
        shape = (FRAME_HEIGHT, FRAME_WIDTH, CHANNEL)
        cameraFeed = np.zeros(shape, np.uint8)
        imgSize = cameraFeed.size
        sockData = b''
        result = True

        while imgSize:
            nbytes=conn.recv(imgSize)
            if not nbytes: break; result = False
            sockData+=nbytes
            imgSize-=len(nbytes)

        if result and imgSize == 0:
            cameraFeed = socketToNumpy(cameraFeed, sockData)
            #cv2.imwrite((os.getcwd()+'/test_images/img.png'),cameraFeed)
            result = False
            running = False
            # Create a window for display.
            #cv2.namedWindow("server");
            #cv2.imshow("server", cameraFeed)
            #key = cv2.waitKey(30)
            #running = key

            # esc
            #if key==27:
                #running =False
    return cameraFeed
    
def FBData(message):
    global conn
    conn.send(bytes(message,encoding="utf-8"))
    conn.close()
    
