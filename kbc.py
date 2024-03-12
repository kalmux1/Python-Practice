
# ! KBC game in python program

ques = ["What is 127.0.0.1","Who is Kalmux","What is Decon Framework","Command for clearing terminal"]
ans= ["Loopback Address","Nitin Jaiswal","Domain Reconnaisance Tool","clear"]
score=0
i = 0

# 
for i in range (len(ques)):
    print(ques[i])
    opt=input("Enter Your Answer: ")
    if (opt == ans[i]):
        score = score +1
        print("CORRECT ANSWER")
        continue
        i=i+1
    else:
        print("wrong answer")
        break

print(" Your Score Is : ",score)
    