username = str(input("Enter username: "))

if len(username) > 15:
    print("Too long")
elif len(username) < 3:
    print("Too short")
else:
    print("Valid")