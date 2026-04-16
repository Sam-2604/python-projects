guess = int(input("Guess a number between 1 and 10: "))

while guess != 7:
    if guess > 7:
        print("Too high")
    elif guess < 7: 
        print("Too low")
    guess = int(input("Guess a number between 1 and 10: "))
    
print("Correct!")