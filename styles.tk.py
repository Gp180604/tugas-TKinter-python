import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text="FLAT", relief=tkinter.FLAT)
B2 = tkinter.Button(top, text="RAISED", relief=tkinter.RAISED)
B3 = tkinter.Button(top, text="SUNKEN", relief=tkinter.SUNKEN)
B4 = tkinter.Button(top, text="GROOVE", relief=tkinter.GROOVE)
B5 = tkinter.Button(top, text="RIDGE", relief=tkinter.RIDGE)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()

top.mainloop()