import cv2

img= cv2.imread("solarsystem.jpg")

cv2.putText(img,"Sun",(100,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(0,0,255))

cv2.putText(img,"MERCURY",(110,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"VENUS",(190,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"EARTH",(285,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"MARS",(380,175),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"JUPITER",(550,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))

cv2.putText(img,"SATURN",(800,310),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"URANUS",(970,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.putText(img,"NEPTUNE",(1110,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(4000)
cv2.imwrite("SS.jpg",img)