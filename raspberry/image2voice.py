
"""
Edge Detection, is an Image Processing discipline that incorporates mathematics methods to find edges in a Digital Image. Edge Detection internally works by running a filter/Kernel over a Digital Image, which detects discontinuities in Image regions like stark changes in brightness/Intensity value of pixels. There are two forms of edge detection:

    Search Based Edge detection (First order derivative)
    Zero Crossing Based Edge detection (Second order derivative)

Some of the commonly known edge detection methods are:

    Laplacian Operator or Laplacian Based Edge detection (Second order derivative)
    Canny edge detector (First order derivative)
    Prewitt operator (First order derivative)
    Sobel Operator (First order derivative)

There are two ways in which we would be implementing Edge detection on our images. In the first method we would be using an inbuilt method provided in the pillow library (ImageFilter.FIND_EDGES) for edge detection. In the second one we would be creating a Laplacian Filter using PIL.ImageFilter.Kernel(), and then would use that filter for edge detection.

Benefits of using Laplacian:- Fast and decent results. Other common edge detectors like Sobel (first order derivative) are more expensive on computation, as they require finding Gradients in two directions and then Normalizing the results. 

Drawbacks of using laplacian:- Convolving with Laplacian Kernel leads to a lot of noise in the output. This issue is resolved by other Edge Detection methods such as Sobel, Prewitt Operator etc. As they have a built-in Gaussian Blur Kernel in them. Which reduces the noise obtained from the input image. They also lead to more accurate edge detection, due to the higher computation involved into finding them.
"""

from PIL import Image, ImageFilter
from numpy import asarray
from numpy import savetxt
 
 
# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
image = Image.open(r"sample.png")
image = image.resize((36, 36))
 
# Converting the image to grayscale, as edge detection
# requires input image to be of mode = Grayscale (L)
# For a grayscale or b&w image, we have pixel values ranging from 0 to 255. 
#The smaller numbers closer to zero represent the darker shade while the larger numbers closer to 255 represent the lighter or the white shade.
image = image.convert("L")
 
# Method 1: Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)

# summarize some details about the image
print("format ", image.format)
print(image.size)
print(image.mode)
# asarray() class is used to convert
# PIL images into NumPy arrays
numpydata = asarray(image)
 
# <class 'numpy.ndarray'>
print(type(numpydata))

# data
#print(numpydata)
#for row in numpydata:
#    print(row)

#  shape
print(numpydata.shape)
# Method 2: Calculating Edges using the passed laplacian Kernel
# final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
#                                          -1, -1, -1, -1), 1, 0))
 
# Saving the Image Under the name Edge_Sample.png
image.save(r"Edge_Sample.png")

savetxt('test.out', numpydata, delimiter=' ', fmt='%3d', newline='\n\n')

