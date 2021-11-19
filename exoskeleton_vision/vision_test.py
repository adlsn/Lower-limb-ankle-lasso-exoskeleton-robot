import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\adl\\Desktop')

'''read photograph'''

photo=cv2.VideoCapture('IMG_3844.avi')
photo1=cv2.imread('IMG_3842.JPG',cv2.IMREAD_REDUCED_GRAYSCALE_4)
r,c=photo1.shape
# cv2.imshow('test1',photo1)
# cv2.waitKey()
# cv2.destroyAllWindows()


'''位平面分解'''

factor=np.zeros((r,c),dtype=np.uint8)
factor[:,:]=2**7
bit1=cv2.bitwise_and(photo1,factor[:,:])
bit2=bit1
bit1[bit1[:,:]>0]=255
# cv2.imshow('1',bit1[:,:])
# cv2.waitKey()
# cv2.destroyAllWindows()
# cv2.imwrite('test1.jpg',bit1[:,:])
# plt.hist(bit1[:,:])
# plt.show()
output=cv2.adaptiveThreshold(photo1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,3)
# cv2.imshow('2',output)
# cv2.waitKey()
# output1=cv2.equalizeHist(bit1[:,:])
# cv2.imshow('3',output1)
# cv2.waitKey()



'''图像平滑处理'''

'''高斯模糊'''
# photo2=cv2.GaussianBlur(output,(3,3),0)
# cv2.imshow('gaussin',photo2)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''双边滤波'''
photo3=cv2.bilateralFilter(output,5,127,127)
cv2.imshow('s',photo3)
cv2.waitKey()
cv2.destroyAllWindows()
# cv2.imwrite('shuangbian.jpg',photo3)

'''腐蚀'''
# kernal=np.ones((3,3),np.uint8)
# photo4=cv2.erode(photo3,kernal)
# cv2.imshow('ss',photo4)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''Sobel'''
# photo5=cv2.Sobel(photo3,-1,0,1)
# cv2.imshow('111',photo5)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''视频测试'''
fourcc=cv2.VideoWriter_fourcc(*'XVID')
size = (int(photo.get(cv2.CAP_PROP_FRAME_WIDTH)), int(photo.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out=cv2.VideoWriter('huofu.avi',fourcc,20,size)

while (photo.isOpened()):
    ret,frame=photo.read()
    if not ret:
        break
    frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    edges=cv2.Canny(frame1,220,250)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 120)

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            if theta > 85 * np.pi / 180 and theta < 95 * np.pi / 180:
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)


        cv2.imshow('11', frame)
        cv2.waitKey(10)

    out.write(frame)

out.release()




'''Canny'''
# edges=cv2.Canny(photo3,220,250)
# cv2.imshow('ddd',edges)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''霍夫直线'''

# lines=cv2.HoughLines(edges,1,np.pi/180,250)
# for line in lines:
#     rho,theta=line[0]
#     a=np.cos(theta)
#     b=np.sin(theta)
#     x0=a*rho
#     y0=b*rho
#     x1=int(x0+1000*(-b))
#     y1=int(y0+1000*(a))
#     x2=int(x0-1000*(-b))
#     y2=int(y0-1000*(a))
#
#
#
#     if theta>85*np.pi/180 and theta<95*np.pi/180:
#         cv2.line(photo1,(x1,y1),(x2,y2),(0,0,255),1)
#
#
#
#
#
#
#
# cv2.imshow('11',photo1)
# cv2.waitKey()
# cv2.destroyAllWindows()

