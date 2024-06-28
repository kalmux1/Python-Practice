import random

number = random.randint(1,100)

gamerun = True

count = 1

while gamerun :
    guess = int(input(" Guess A NUmber : "))
    if (guess == number):
        print(f"You Guessed The Right Number {number} in {count} guesses")
        gamerun = False
    elif (guess > number):
        print("Lower Number Please")
        count += 1
    elif (guess < number):
        print("Higher Number Please")
        count += 1
    else:
        print("Invalid Input")
