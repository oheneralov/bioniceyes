
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
from pysinewave import SineWave
import time
 
 
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

sinewave = SineWave(pitch = 0, pitch_per_second = 6)

# data
#print(numpydata)
volume = 40
brightness_threshold = 50
counter = 0
pitchesArr = []

#volume = volume - 1
# 1 volume decrease per row
# the lower row the smaller volume
sinewave.set_volume(volume)


for row in numpydata:
    pitchesArr.append(0) # denotes a new row 
    for value in row:
        # pitch depends on x coordinate of n edge point
        if value > brightness_threshold:
            counter = counter + 1
            pitchesArr.append(value)

sinewave.play()
for value in pitchesArr:
    sinewave.set_pitch(value)
    time.sleep(0.01)

sinewave.stop()





#  shape
print("counter ", counter)
# Method 2: Calculating Edges using the passed laplacian Kernel
# final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
#                                          -1, -1, -1, -1), 1, 0))
 
# Saving the Image Under the name Edge_Sample.png
#image.save(r"Edge_Sample.png")
image.close()

#savetxt('test.out', numpydata, delimiter=' ', fmt='%3d', newline='\n\n')


# voice image
"""
https://pypi.org/project/pysinewave/
You may want to directly modify the frequency and amplitude of a SineWave. We do provide two alternative functions, SineWave.set_frequency(hertz) and SineWave.set_amplitude(percent), however we suggest that you use SineWave.set_pitch(pitch) and SineWave.set_volume(decibels) instead.

Why? The brain naturally perceives ratios between sound's frequency and amplitude much better than differences. This means that working directly with frequency will cause high frequencies to be much harder to distinguish than low frequencies. Similarly for amplitude.

The conversion between pitch and frequency (in Hz) is: frequency = 440 * 2^((pitch-9)/2). For instance, note that a pitch of 0 is middle C, i.e. a frequency of 261.63 Hz.

The conversion between volume (in decibels) and amplitude is: amplitude = 2^(volume/10). For instance, increasing the volume by 10 decibels doubles the amplitude of the sine wave.

Here's a helpful table showing the relationship between frequency, pitch, and musical notes for one octave:

Pitch 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12
Frequency 	261.63 	277.18 	293.66 	311.13 	329.63 	349.23 	369.99 	392.00 	415.30 	440.00 	466.16 	493.88 	523.25
Note 	C 	C#/Db 	D 	D#/Eb 	E 	F 	F#/Gb 	G 	G#/Ab 	A 	A#/Bb 	B 	C
"""





