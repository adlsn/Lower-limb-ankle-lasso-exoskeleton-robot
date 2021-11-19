import cv2
import os
import numpy as np

os.chdir('C:\\Users\\adl\\Desktop')

videoin=cv2.VideoCapture('IMG_3844.avi')
_,frametest=videoin.read()
frametest=cv2.adaptiveThreshold(frametest[:,:,0], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 3)
r,c,=frametest.shape
size = (int(videoin.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoin.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc=cv2.VideoWriter_fourcc(*'XVID')
videoput=cv2.VideoWriter('output.avi',fourcc,20,(640,720))

while (videoin.isOpened()):
    ret,frame=videoin.read()
    if ret:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 3)
        figure = cv2.bilateralFilter(frame, 5, 127, 127)
        figure=cv2.resize(figure,(640,720))
        cv2.imshow('1',figure)
        cv2.waitKey(10)
        videoput.write(figure)
    else:
        break
videoput.release()
videoin.release()

'''出问题的是导出视频时的size，编码没有问题！！！'''