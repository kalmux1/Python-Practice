
# * GREETING PROGRAM IN PYTHON

import time

timestamp=int(time.strftime('%H'))

print(" KALMUX AI ")

if(timestamp >= 22 and timestamp < 5 or timestamp == 00):
    print(" GOOD NIGHT SIR !")
elif(timestamp >= 12 and timestamp < 16):
    print(" GOOD AFTERNOON SIR !")
elif(timestamp >= 16 and timestamp < 22):
    print(" GOOD EVENING SIR !")
elif(timestamp >= 5 and timestamp < 12):
    print(" GOOD MORING SIR !")
else:
    print(" AI ERROR SIR !")
