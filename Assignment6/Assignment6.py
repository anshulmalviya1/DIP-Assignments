from PIL import Image
from PIL import ImageEnhance


image = Image.open('img.jpg')
image.show()

# Enhance Contrast
curr_con = ImageEnhance.Contrast(image)
new_con = 3

# Contrast enhanced by a factor of 3
img_contrasted = curr_con.enhance(new_con)
img_contrasted.show()
