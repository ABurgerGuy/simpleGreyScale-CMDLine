import sys
from PIL import Image, ImageFilter

#Made by : Burg
#Date : 10/18/2020
#Description : This is a simple command line program that takes in two arguments from command prompt.
#              The first argument that's taken in is the name of the input image and the second
#              argument is the name of the desired output image. The output image can be overwritten
#              so do be careful.

inputIMG = sys.argv[1]
outputIMG = sys.argv[2]
print("taking : "+ inputIMG + "\nand cahnging it to : " + outputIMG)


image = Image.open(inputIMG)

image = image.convert("L")

#image = image.filter(ImageFilter.FIND_EDGES)

image.save(outputIMG)
