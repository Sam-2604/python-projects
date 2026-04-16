total = 0
user_input = input("Enter a number: ")  # first ask, before loop

while user_input != "stop":
    total = total + int(user_input)
    user_input = input("Enter a number: ")  # ask again each iteration

print(total)