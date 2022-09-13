# Package: Pillow
from PIL import Image

h1 = Image.open("img/h1.png")
c1 = Image.open("img/c1.png")
c2 = Image.open("img/c2.png")
c3 = Image.open("img/c3.png")
s1 = Image.open("img/s1.png")
s2 = Image.open("img/s2.png")

heads = [h1]
caps = [c1,c2,c3]
shirts = [s1,s2]

for cap in range(3):
    for shirt in range(2):
        new_image = Image.new('RGBA',(16, 16), (250,250,250,0))
        new_image.paste(heads[0],(0,0))
        new_image.paste(caps[cap],(0,0),caps[cap])
        new_image.paste(shirts[shirt],(0,0),shirts[shirt])
        new_image.save("dude{}{}.png".format(cap,shirt))
