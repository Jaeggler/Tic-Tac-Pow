import tkinter as tk
from tkinter import *


root = tk.Tk()
frame = Frame(root, bg = "red")
frame.pack()

bottomframe = Frame(root, bg = "blue")
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red",bg="grey", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()