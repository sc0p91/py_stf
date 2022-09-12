# Package: Pillow
from PIL import Image

im1 = Image.open("img/head.png")
im2 = Image.open("img/hat.png")

new_image = Image.new('RGBA',(1000, 1000), (250,250,250,0))
new_image.paste(im1,(150,200))
new_image.paste(im2,(00,-250),im2)
new_image.show()
new_image.save("img/rock.png")
