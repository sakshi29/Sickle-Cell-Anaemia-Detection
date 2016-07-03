############################################
## Import OpenCV
import numpy as np
import cv2
from matplotlib import pyplot as plt

############################################

############################################
## Read the image
img= cv2.imread('SCA.jpg')
############################################

############################################
## Do the processing
############################################
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##ret,thresh1 = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
##ret,thresh4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
##print img
im_floodfill = thresh2.copy()
h, w = thresh2.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
im_out = thresh2 | im_floodfill_inv
##pix_val=list
m=[]
contours, hierarchy = cv2.findContours(im_out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(0,len(contours)):
    
    cv2.drawContours(img,contours,i,(0,255,0),3)
    area =cv2.contourArea(contours[i])
    perimeter =cv2.arcLength(contours[i],True)
    if( area==0 or perimeter==0):
        continue
    a=( 4 * 3.14 * area )/(perimeter*perimeter)
    m.append(a)
    ##print area
    ##print perimeter
f=1    
for j in range (0,len(m)):
    if(m[j]<0.70):
       f=0 
      ##print "anomoly"
      ##print m[j]
if(f==0):
   print 'anomaly detected sickel cell present'
else:
   print 'healthy cells'
  
############################################
## Show the image
cv2.imshow('image',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
