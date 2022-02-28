import glob
import os
import shutil
import tkinter
from tkinter import *

import PIL
from PIL import Image, ImageTk


def image():  # sourcery skip: remove-redundant-if

    pic = 'nasa_pics/NasaPic.jpg'
    #pic = "nasa_pics/nasa3.jpg"
    image = PIL.Image.open(pic)

    Width,height = image.size
    
    if height >= 1100:
        height = 1030
    
    if Width >= 1921:
        Width = 1920
    
    newH = height

    print(Width, newH)
    
    
    def save_pic():
        src_dir = "nasa_pics"
        dst_dir = "saved"
        for jpgfile in glob.iglob(os.path.join(src_dir, "NasaPic.jpg")):
            shutil.copy(jpgfile, dst_dir)
    
    root = Tk()
    root.iconbitmap("ponyo.ico")
    root.title("ponko")
    canvas = Canvas(root, width = Width, height = newH)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(pic))
    print(pic)
    canvas.create_image(0, 0, anchor=NW, image=img)
    save_button = tkinter.Button(root, text="save pic", command=save_pic)
    save_button.pack()
    root.mainloop() 

print("befor gard")
if __name__ == "__main__":
    image()
