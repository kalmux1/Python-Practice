# COLLEGE ADMISSION FORM

from tkinter import *

base = Tk()

base.configure(bg="darkgrey")
base.title(" COLLEGE ADMISSION FORM ")

base.geometry("600x400")
base.maxsize(width=600, height=400)

head_frame = Frame(base, relief=SUNKEN, bg="lightgrey", borderwidth=4,padx=207)
head_frame.pack(side=TOP)

head_tittle = Label(head_frame, text=" COLLEGE ADMISSION FORM ", fg="black",bg="lightgrey")
head_tittle.pack(pady=2)

body_frame = Frame(base, relief=SUNKEN, borderwidth=4, padx=20 , pady= 50)
body_frame.pack(padx=6,pady=10, fill=BOTH, expand=True)

Fname = Label(body_frame, text=" FIRST NAME ")
Fname.grid(row=1,column=0, pady= 5,padx=10, sticky=E)

fnamevalue = StringVar()
fnameinput = Entry(body_frame, textvariable= fnamevalue, width=25)
fnameinput.grid(row=1, column=1, padx= 5)

Lname = Label(body_frame, text=" LAST NAME ")
Lname.grid(row=1,column=3, pady=5,padx=10, sticky=E)

lnamevalue = StringVar()
lnameinput = Entry(body_frame, textvariable= lnamevalue,width=25)
lnameinput.grid(row=1, column=4, padx=5)

Age = Label(body_frame, text=" AGE ")
Age.grid(row=2 ,padx=10,pady=5)

agevalue = StringVar()
ageinput = Entry(body_frame, textvariable= agevalue,width=25)
ageinput.grid(row=2, column=1, pady=10)


dob = Label(body_frame, text=" DOB ")
dob.grid(row=2,column=3)

dobvalue = StringVar()
dobinput = Entry(body_frame, textvariable= dobvalue, width=25)
dobinput.grid(row=2, column=4, pady=5,padx=10)

add = Label(body_frame, text=" ADDRESS ")
add.grid(row=3, padx=10,pady=5)

addvalue = StringVar()
addinput = Entry(body_frame, textvariable= addvalue, width= 69)
addinput.grid(row=3, column=1,columnspan=4)

def getvals():
    pass


submit = Button(body_frame, text="SUBMIT" , command=getvals ,padx=15,relief=RAISED)
submit.grid(row=4,column=0, pady=80, columnspan=5)

base.mainloop()