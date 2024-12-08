from tkinter import *

top = Tk()
Lb1 = Listbox(top)
Lb1.insert(1, "kucing")
Lb1.insert(2, "kelinci")
Lb1.insert(3, "jerapah")
Lb1.insert(4, "gajah")
Lb1.insert(5, "ular")
Lb1.insert(6, "kadal")
Lb1.pack()
top.mainloop()