# This python file is for Tkinter GUI Practice

from tkinter import *

root = Tk()

root.title("KALMUX")

root.geometry("833x534")

photo = PhotoImage(file="E:\GITHUB\Python-Practice\GUI\wp.png")
bg = Label(image=photo)
bg.pack()
kalmux = Label(root, text="KALMUX GUI", padx=10, pady=10, relief=RAISED)
kalmux.pack(anchor="center")

root.mainloop()