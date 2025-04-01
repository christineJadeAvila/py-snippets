import rembg
import numpy as np
from PIL import Image

# Load the input image 
inputImage = Image.open('sample.webp')

# convert RGBA to RGB
rgb_im = inputImage.convert('RGBA')

# convert the inputted image to a numpy array
inputArray = np.array(rgb_im)

#  apply background removal using rembg
outputArray = rembg.remove(inputArray)

# create a PIL Image from the output array
outputImage = Image.fromarray(outputArray)

# save the output image
outputImage.save('outputImage1.png')