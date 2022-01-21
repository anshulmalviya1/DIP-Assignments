from matplotlib.image import imread
import matplotlib.pyplot as plt


inpimg = imread("Img.jpg")
r,g,b = inpimg[:,:,0], inpimg[:,:,1], inpimg[:,:,2]
gamma: float = 1.04
r_const = 0.2026
g_const = 0.7152
b_const = 0.0772


greyimg = r_const*r**gamma + g_const*g**gamma + b_const*b**gamma
fig = plt.figure(1)


img = fig.add_subplot(111)
img.imshow(greyimg, cmap=plt.cm.get_cmap('Greys'))


fig.show()
plt.show()
