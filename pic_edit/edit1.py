
from PIL import Image,ImageEnhance, ImageFilter
import os
# img1 = Image.open("dog.jpg")

# img1.save("dog.png")
# img1.show()

# resize

# MAX_SIZE = (600,600)
# img1.thumbnail(MAX_SIZE)
# img1.save("dogsmall.png")
# for list in os.listdir():
#     if list.endswith(".jpg"):
#         img1 = Image.open(list)
#         filename,extension = os.path.splitext(list)
#         img1.save(f"{filename}.png")

# increase sharpness
img1 = Image.open("background.png")
MAX_SIZE = (288,512)
img1.thumbnail(MAX_SIZE)
img1.save("background.png")
# Enchance = ImageEnhance.Sharpness(img1)
# Enchance.enhance(3.5).save("dog1x.jpg")

# # color class
# img2 = Image.open("dog1x.jpg")
# Enchance = ImageEnhance.Color(img2)
# Enchance.enhance(1.3).save("dog2x.jpg")
# # brigthness
# img3 = Image.open("dog2x.jpg")
# Enchance = ImageEnhance.Brightness(img3)
# Enchance.enhance(1.1).save("dog3x.jpg")
# # contrast
# img4 = Image.open("dog3x.jpg")
# Enchance = ImageEnhance.Contrast(img4)
# Enchance.enhance(1.15).save("dog4x.jpg")

# # image blur
# img1.filter(ImageFilter.GaussianBlur(radius=4)).save("blurred.png")
