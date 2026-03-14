# Language: Python

# Import kivy App and widgets
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Define the main widget of the app
class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set the orientation of the layout (vertical/horizontal)
        self.orientation = 'vertical'

        # Create a label
        self.my_label = Label(text="Hello, Kivy!", font_size=32)
        self.add_widget(self.my_label)

        # Create a button and bind it to a function
        self.my_button = Button(text="Click Me", size_hint=(1,0.2))
        self.my_button.bind(on_press=self.on_button_click)
        self.add_widget(self.my_button)

    # Define the button action
    def on_button_click(self, instance):
        self.my_label.text = "Button Clicked!"

# Define the App class
class MyKivyApp(App):
    def build(self):
        return MyBoxLayout()  # Return the root widget

# Usage
if __name__ == "__main__":
    MyKivyApp().run()