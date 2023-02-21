import random
import time
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class CameraClick(BoxLayout):
  def capture(self):
      '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
      # self.cameraObject = Camera(play=True,resolution=(640,480),index=0)
      # self.cameraObject.export_to_png('./selfie.png')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 2000))


class Main(App):
  def build(self):
      """
            label = Label(text='Hello from Kivy',
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
      return label
      """
      return MyRoot()



randomApp = Main()
randomApp.run()
