from tkinter import *
import ttkbootstrap as ttk

# mainwindow
win = ttk.Window(themename= "darkly")
win.title("Canvas")
win.geometry("500x380")

# canvas window
Canvas = ttk.Canvas(win, bg = "white")
Canvas.pack()

Canvas.create_oval((200,0,300,100), fill= "white") # oval shape
Canvas.create_arc((200,0,300,100), fill= "blue", start= 45, extent = 140, style = ttk.PIESLICE, outline = "pink", width = 1) #Arc shape

# Run function
mainloop()