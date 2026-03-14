"""
simple_kivy_training.tryKivy_
"""
# ----------------------------------------------------------------------------------------------------------------------
'''
Application example using build() + return
==========================================

An application can be built if you return a widget on build(), or if you set
self.root.
'''

# ----------------------------------------------------------------------------------------------------------------------
import time
'''import kivy
if kivy.__version__ >= '%d.%d.%d' % (2, 0, 0):
  ...
else:
  kivy.require('1.0.7')'''
# kivy application -> [app](App)
from kivy.app import App
# kivy animations -> [animation](Animation)
#from kivy.animation import Animation
#from kivy.lang import Builder # Language
# kivy UI/UX -> [uix](*)
#from kivy.uix.actionbar import ActionBar
#from kivy.uix.accordion import Accordion
from kivy.uix.button import Button
#from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
#from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
#from kivy.uix.camera import Camera
#from kivy.uix.image import Image
#from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
# import kivy.properties as kv_p
#from kivy.utils import hex_colormap, rgba
#from kivy.input.provider import MotionEventProvider"""
# kivy events -> [event]
# from kivy.event import EventDispatcher
# from kivy._event.EventDispatcher import bind

# ----------------------------------------------------------------------------------------------------------------------
class Kivy1Sys_():
  def __init__(self, ):
    pass

  def _prevent(self, instance):
    print(f" :-- Cursor focusing on textinput field --: ")

  def _react(self, instance):
    print(f" I were clicked to do something great !\n (exit_code={1}) ")

# -----------------------------------------------------------
class Kivy1App_(App):
  kv_sys_ = Kivy1Sys_()

  def build(self, ):
    # init ----------------------------------------------->
    global text_
    text_ = ["Hello World _", "Bienvenue dans notre Application _", "Sample Interactive Kivy App. _"]
    ROWS_, COLS_, GRID_LIM = 3, 3, 3
    SCREEN_WIDTH = 640, 621
    
    self.window_ = GridLayout(
      rows=ROWS_, cols=COLS_, col_default_width=640,
      # size_hint_min=(0.7, 0.8), size_hint_max=(0.9, 1.0),
      size_hint=(0.75, 0.85),
      pos_hint={"center_x": 0.5, "center_y": 0.5},
    ) # return a GridLayout() as a root Layout
    
    # CREATING WIDGETS ----------------------------------->
    for label_n in range(GRID_LIM):
      self.window_.add_widget(
        Label(text=f"{text_[label_n+0]}", )
      )
    #
    self.text1input_ = TextInput(
      center=(self.window_.get_center_x()/2, self.window_.get_center_y()/2),
      height=121, font_size=16, multiline=False,
      background_color="#fffffca8",
      #on_double_tap=self.kv_sys_._prevent,
    ) # return a TextInput() as a child widget
    self.text1input_.bind(on_double_tap=self.kv_sys_._prevent, )
    #
    self.button_ = Button(
      text=f"{text_[0]}",
      height=121, font_size=14, background_color="#fffffc6d",
      on_press=self.kv_sys_._react,
    ) # return a Button() as a child widget
    #self.button_.bind(on_press=self.kv_sys_._react, )
    # self.OBJECT.bind(_f_=func_) | func_ not func_() -> None (not callable)

    # ADDING OBJECTS TO DISPLAYS ------------------------->
    self.window_.add_widget(self.text1input_, )
    self.window_.add_widget(self.button_, )

    # return super().build() ----------------------------->
    return self.window_
  """(
      self.button_,
    )"""
  
  def callback_(self, instance, ):
    ...
  #

# ----------------------------------------------------------------------------------------------------------------------
'''
root = Accordion(min_space=60)

# unicode text; can only display glyphs that are available in the font
l = Label(text='Hello world ' + chr(2764))
l_ = Label(text='Hello world', font_size='20sp')
'''
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
  kv_app = Kivy1App_()
  kv_app.run()
  time.sleep(1.2)
  """kv_sys = Kivy1Sys_()
  kv_sys.run()"""
#
