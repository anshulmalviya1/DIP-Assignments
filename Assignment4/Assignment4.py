
# In[1]
# Show image
import cv2
import numpy as np
 
img_path = r"img.jpg"
img = cv2.imread(img_path)
img = cv2.resize(img, (1157, 664))
cv2.imshow("Color Image", img)


img.shape


b, g, r = cv2.split(img)
zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
blue_img = cv2.merge([b, zeros_ch, zeros_ch])
cv2.imshow("Blue Image", blue_img)

green_img = cv2.merge([zeros_ch, g, zeros_ch])
cv2.imshow("Green Image", green_img)

 
red_img = cv2.merge([zeros_ch, zeros_ch, r])
cv2.imshow("Red Image", red_img)


 
img = cv2.resize(img, (400,300))
red_array = np.zeros(img.shape, dtype="uint8")
red_array[:,:,2] = img[:,:,2]
green_array = np.zeros(img.shape, dtype="uint8")
green_array[:,:,1] = img[:,:,1]
blue_array = np.zeros(img.shape, dtype="uint8")
blue_array[:,:,0] = img[:,:,0]
cv2.waitKey(0)
