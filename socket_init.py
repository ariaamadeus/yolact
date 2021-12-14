import socket
import cv2
import numpy as np

def sendInit():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "192.168.5.73"
    port = 7002
    s.connect((host,port))
    s.send(cv2.imencode('.jpg',(np.ndarray((2000, 2000, 3), dtype=int)).astype(np.uint8))[1].tobytes)
    s.close()
