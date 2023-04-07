from PIL import Image , ImageChops

img1 = Image.open("img_1.jpg")
img2= Image.open("img_2.jpg")





diff = ImageChops.difference(img1 , img2)
img1.show()
img2.show()




if diff.getbbox():
    diff.show()
