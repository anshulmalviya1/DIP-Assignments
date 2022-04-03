import cv2
import numpy as np

original = cv2.imread('img.jpg')

imageHeight = len(original)
imageWidth = len(original[0])

gray = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth): 
        gray[i][j] = int(original[i][j][0] * 0.2126 + original[i][j][1] * 0.7152 + original[i][j][2] * 0.0722)

sub = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        sub[i][j] = int(original[i][j][0] * 0.2126 + original[i][j][1] * 0.7152 + original[i][j][2] * 0.0722)

for i in range(250, imageHeight-250):
    for j in range(250, imageWidth-250):
        sub[i][j] = int(original[i][j][0] * 0 + original[i][j][1] * 0 + original[i][j][2] * 0)


cv2.imshow('Original', original)              
cv2.imshow('gray', gray)
cv2.imshow('Some black', sub)  
cv2.imshow('Substraction',gray-sub)            
cv2.waitKey(0)