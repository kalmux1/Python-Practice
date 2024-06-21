
# TAX MANAGEMENT SYSTEM
#

print(" \nTAX MANAGEMENT SYSTEM ")
print("\n")
print(" 1 - BELOW 20K ")
print(" 2 - ABOVE 20K BUT BELOW 50K")
print(" 3 - ABOVE 50K BUT BELOW 75K ")
print(" 4 - ABOVE 75K BUT BELOW 90K ")
print(" 5 - ABOVE 90K \n")
salary=int(input(" ENTER ONE OPTION :-  "))

match salary :
    case 1:
        print(" YOU DON'T HAVE TO PAY TAX ")
    case 2:
        print(" YOU HAVE TO PAY 10% TAX ")
    case 3:
        print(" YOU HAVE TO PAY 15% TAX ")
    case 4:
        print(" YOU HAVE TO PAY 20% TAX ")
    case 5 :
        print(" YOU HAVE TO PAY 25% TAX ")
    case _:
        print(" INVALID OPTION ")




