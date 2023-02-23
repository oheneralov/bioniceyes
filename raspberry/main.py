
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


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from PIL import Image, ImageFilter
import time
import numpy
from pysinewave import SineWave


if ( platform == 'android' ):
    from android.permissions import request_permissions, Permission
    request_permissions([
    Permission.CAMERA,
    Permission.WRITE_EXTERNAL_STORAGE,
    Permission.READ_EXTERNAL_STORAGE
])




Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        index: 0
        id: camera
        resolution: (30,30)
        play: True
        allow_stretch: True
        canvas.before:
            PushMatrix
            Rotate:
                angle: -90
                origin: self.center
        canvas.after:
            PopMatrix
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
    
''')


class CameraClick(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        texture = camera.texture
        pixels = texture.pixels
        print("pixels are ", len(pixels))
        pil_image=Image.frombytes(mode='L', size=(30,30), data=pixels)
        numpypicture=numpy.array(pil_image)
        print(numpypicture)
        volume = 40
        brightness_threshold = 50
        counter = 0
        pitchesArr = []
        sinewave.set_volume(volume)
        for row in numpypicture:
            pitchesArr.append(0) # denotes a new row 
            counter = 0
            for value in row:
            # pitch depends on x coordinate of n edge point
                if value > brightness_threshold:
                    counter = counter + 1
                    pitchesArr.append(counter)

        sinewave.play()
        for value in pitchesArr:
            sinewave.set_pitch(value)
            time.sleep(0.01)

        sinewave.stop()

# Method 2: Calculating Edges using the passed laplacian Kernel
# final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
#                                          -1, -1, -1, -1), 1, 0))
 
# Saving the Image Under the name Edge_Sample.png
#image.save(r"Edge_Sample.png")

#savetxt('test.out', numpydata, delimiter=' ', fmt='%3d', newline='\n\n')


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()

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