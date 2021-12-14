import os
import torch
import json

import socket_server as ss

import eval

''' Functions
ss.startServer(HOST, PORT)
ss.recvData(s)
ss.FBData(message)
eval.outEval(score_threshold, top_k, image, cuda = True)
eval.theInit(trained_model, config, ifinit = False, cuda = True)
'''

HOST = "192.168.5.73"
PORT = 7002
CONFIG = "yolact_resnet50_kelapa_sawit_config"
MODEL = "weights/yolact_plus_resnet50_kelapa_sawit_77_544_interrupt.pth"
score_threshold=0.5
top_k=1
labels = ['Accept','Reject']
#images="test_images:output_image"

eval.theInit(MODEL, CONFIG, True)
s = ss.startServer(HOST,PORT)

while True:
    camFeed = ss.recvData(s)
    result = eval.outEval(score_threshold, top_k,camFeed)
    classes = labels[(result[0][0].tolist())[0]]
    scores = (result[1][0].tolist())[0]
    
    print('Result:',classes,'Scores:',scores)
    ss.FBData(json.dumps({"classes":classes,"scores":scores}))
    #ss.FBData(json.dumps({"classes":labels[(result[0][0].tolist())[0]],"scores":result[1][0].tolist(),"boxes":result[2][0].tolist()}))
