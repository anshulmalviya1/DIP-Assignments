import cv2
import numpy as np

orginal = cv2.imread('Input_img.jpeg')

imageHeight = len(orginal)
imageWidth = len(orginal[0])

gray = np.zeros((imageHeight, imageWidth), dtype=np.uint8)


for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        gray[i][j] = int(orginal[i][j][0] * 0.2126 + orginal[i][j][1] * 0.7152 + orginal[i][j][2] * 0.0722)

binary = np.zeros((imageHeight, imageWidth), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        if gray[i][j] >= 127:
            binary[i][j] = 255
        else:
            binary[i][j] = 0

rgb = np.zeros((imageHeight, imageWidth, 3), dtype=np.uint8)

for i in range(0, imageHeight):
    for j in range(0, imageWidth):
        rgb[i][j] = orginal[i][j] + np.uint(20)

cv2.imshow('Orginal', orginal)
cv2.imshow('Gray', gray)              
cv2.imshow('Binary', binary)             
cv2.imshow('RGB + 20', rgb)         
cv2.imshow('Gray + Binary',gray+binary)    
cv2.waitKey(0)