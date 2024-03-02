
# PYTHON CALCULATOR

# ! STARTING THE CALCULATOR

print(" ") 
print(" PYTHON CALCULATOR ")
print(" ")
num1= float(input(" ENTER FIRST NUMBER :- "))
num2= float(input(" ENTER SECOND NUMBER :- "))
print(" ")
print(" [+] - ADDITION ")
print(" [-] - SUBTRACTION ")
print(" [*] - MULTIPLICATION ")
print(" [/] - DIVISION ")
print(" ")
opr= input(" ENTER THE OPERATION :- ")
print(" ")

if(opr == "+"):
    result = num1 + num2
    print(" THE ADDITION IS :- ",result)
elif(opr == "-"):
    result = num1 - num2
    print(" THE SUBTRACTION IS :- ", result)
elif(opr == "*"):
    result = num1 * num2
    print(" THE MULTIPLICATION IS :- ",result)
elif(opr == "/"):
    result = num1 / num2
    print(" THE DIVISION IS :- ",result)
else:
    print(" INVALID OPERATION ")
