from tkinter import *
import tkinter.messagebox

top = Tk()
C = Canvas(top, bg="blue", height=350, width=350)

filename = PhotoImage(file="gambar.gif")
image = C.create_image(180, 300, anchor=S, image=filename)

C.pack()
top.mainloop()