
# TAX MANAGEMENT SYSTEM
#

print(" TAX MANAGEMENT SYSTEM ")
print(" ")
salary=float(input(" ENTER YOUR SALARY :- "))

match salary:

    case _ if salary >= 20000:
        print(" YOU DON'T HAVE TO PAY TAX")
        
    case _  if salary >= 20000 and salary < 50000:
        print(" YOU HAVE TO PAY 10% TAX")

    case _ if salary >= 50000 and salary < 75000:
        print(" YOU HAVE TO PAY 15% TAX")

    case _ if salary >= 75000 and salary < 90000:
        print(" YOU HAVE TO PAY 20% TAX")

    case _ if salary <= 90000:
        print(" YOR HAVE TO PAY 25% TAX ")
