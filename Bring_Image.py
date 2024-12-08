from tkinter import *

root = Tk()  # Membuat jendela utama aplikasi

# Membuat kanvas dengan ukuran 300x200 piksel dan warna latar belakang kuning
canvas = Canvas(width=300, height=200, bg='yellow')

# Menempatkan kanvas ke dalam jendela utama agar terlihat
canvas.pack(expand=YES, fill=BOTH)

# Memuat gambar GIF (ganti 'dw.gif' dengan nama file gambar Anda)
gif1 = PhotoImage(file='gambar.gif')

# Menempatkan gambar GIF pada kanvas dengan posisi pojok kiri atas (NW) di koordinat (50, 10)
canvas.create_image(50, 10, image=gif1, anchor=NW)

# Menjalankan aplikasi
root.mainloop()