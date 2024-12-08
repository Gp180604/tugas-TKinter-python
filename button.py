import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showwarning("Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command=helloCallBack)
B.pack()  # Menambahkan tombol ke jendela

top.mainloop()