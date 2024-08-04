# This python file is for Tkinter GUI Practice

from tkinter import *

base = Tk()

base.title("KALMUX")

base.geometry("733x434")

# photo = PhotoImage(file="E:\GITHUB\Python-Practice\GUI\wp.png")
# bg = Label(image=photo)
# bg.pack()

frame1 = Frame(base, borderwidth=9 , padx=210 , relief=SUNKEN , bg="lightgrey")
frame1.pack(side=TOP, fill=X)
kalmux = Label(frame1, text="KALMUX GUI", fg="black", bg="lightgrey")
kalmux.pack(anchor="center", padx=110)

frame2 = Frame(base, relief=SUNKEN, borderwidth=3, pady=180, padx=25, bg="lightgrey")
frame2.pack(side=LEFT, fill=Y)
content = Label(frame2, text="CONTENT", fg="black", bg="lightgrey")
content.pack(side=TOP, anchor="ne")

frame3 = Frame(base,borderwidth=3, relief=SUNKEN, bg="lightgrey")
frame3.pack(anchor="center")

b1 = Button(frame3, text="button")
b1.pack(anchor="center")
base.mainloop()