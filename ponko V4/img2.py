import glob
import os
import shutil

from kivy.app import App
from kivy.graphics import *
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from datetime import date
Builder.load_file('kivy_img.kv')

class MyLayout(Widget):
    pass

    def save_pic(self):  # sourcery skip: sum-comprehension
        src_dir = "nasa_pics"
        dst_dir = "saved"
        temp_dir = "tempPic"
        time = date.today()
        newName = rf"tempPic/NasaPic{date.day}.jpg"
        # you get it right one of the times you did it but i have no clue when that was but it was the time when we used the couter i think
        os.mkdir(temp_dir)
        
        for jpgfile in glob.iglob(os.path.join(src_dir, "NasaPic.jpg")):
            shutil.move(jpgfile, temp_dir)
        
        os.rename(r"tempPic/NasaPic.jpg", rf"tempPic/NasaPic M.{time.month},D.{time.day}.jpg")
        shutil.move(rf"tempPic/NasaPic M.{time.month},D.{time.day}.jpg", dst_dir)
        os.removedirs(temp_dir)
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.save = Button(text='Save')
        self.save.bind(on_press=self.save_pic)
        self.add_widget(self.save)
        

class MyApp(App):

    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
