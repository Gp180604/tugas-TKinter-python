import tkinter
import tkinter.messagebox

top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 100,10,1000,1000
arc = C.create_arc(coord, start=0, extent=200, fill="red")
C.pack()
top.mainloop()