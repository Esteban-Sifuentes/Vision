from Tkinter import *
from PIL import ImageTk, Image

path = 'mugrero.jpg'

root = Tk()
img = ImageTk.PhotoImage(Image.open(path))
texto = """Little
ball
of fur"""

w = Label(root, 
             compound = CENTER,
             text = texto,
             image = img).pack(side='right')

root.mainloop()
