
# * B9AISC LOGIN PROGRAM

print(" WELCOME TO THE LOGIN PORTAL OF KALMUX ")
print("\n")
username=input(" ENTER THE USERNAME :- ")
password=input(" ENTER THE PASSWORD :- ")

# ! CONVERTING USERNAME IN LOWERCASE

user=username.lower()

# ? CHECKING OF THE USERNAME AND PASSWORD

if ( user == "kalmux" and password == "kalmux123" ):
    print(" \nLOGIN SUCCESSFULL ! ")
else:
    print(" \nLOGIN UNSUCCESSFULL ! ")
