# COLLEGE ADMISSION FORM

from tkinter import *

base = Tk()


base.title(" COLLEGE ADMISSION FORM ")

base.geometry("600x400")
base.maxsize(width=600, height=400)

head_frame = Frame(base, relief=SUNKEN, bg="lightgrey", borderwidth=4,padx=207)
head_frame.pack(side=TOP)

head_tittle = Label(head_frame, text=" COLLEGE ADMISSION FORM ", fg="black",bg="lightgrey")
head_tittle.pack(pady=2,)

body_frame = Frame(base, relief=SUNKEN, borderwidth=4, padx=190 , pady= 120)
body_frame.pack(pady=10,anchor="center")

Fname = Label(body_frame, text=" FIRST NAME ")
Fname.grid(row=1, sticky="nw")

fnamevalue = StringVar()
fnameinput = Entry(body_frame, textvariable= fnamevalue)
fnameinput.grid(row=1, column=1)

Lname = Label(body_frame, text=" LAST NAME ")
Lname.grid()

lnamevalue = StringVar()
lnameinput = Entry(body_frame, textvariable= lnamevalue)
lnameinput.grid(row=2, column=1)

Age = Label(body_frame, text=" FIRST NAME ")
Age.grid()

agevalue = StringVar()
ageinput = Entry(body_frame, textvariable= agevalue)
ageinput.grid(row=3, column=1)

add = Label(body_frame, text=" ADDRESS ")
add.grid()

addvalue = StringVar()
addinput = Entry(body_frame, textvariable= addvalue)
addinput.grid(row=4, column=1)

def getvals():
    pass


submit = Button(body_frame, text="SUBMIT" , command=getvals)
submit.grid(row=5,column=1, pady=10)

base.mainloop()