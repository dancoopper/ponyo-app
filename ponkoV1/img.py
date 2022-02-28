from tkinter import *  
import PIL
from PIL import ImageTk,Image

def image():  # sourcery skip: remove-redundant-if

    pic = 'nasa_pics/NasaPic.jpg'
    #pic = "nasa_pics/nasa3.jpg"
    image = PIL.Image.open(pic)

    Width,height = image.size
    
    if height >= 1094:
        height = 1030
    
    if Width >= 1921:
        Width = 1920
    
    newH = height

    print(Width, newH)


    root = Tk()
    root.iconbitmap("ponyo.ico")
    root.title("ponko")
    canvas = Canvas(root, width = Width, height = newH)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(pic))
    print(pic)
    canvas.create_image(0, 0, anchor=NW, image=img)
    root.mainloop() 

print("befor gard")
if __name__ == "__main__":
    image()