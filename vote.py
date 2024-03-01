
# PYTHON PROGRAME FOR VOTE


print(" ") 
print(" WLCOME TO VOTING RIGHT PORTAL")
print(" ")
age = int(input(" ENTER YOUR AGE :- "))

if(age >= 0 and age <= 18):
    print("")
    print(" YOU CANNOT VOTE")
elif(age >= 18 and age <=110):
    print(" ")
    print(" YOU CAN VOTE ")
else:
    print(" ")
    print(" INVALID AGE ")
