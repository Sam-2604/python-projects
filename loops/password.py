count = 0

while True:
    password = input("Enter password: ")
    if password == "python123":
        print("Correct")
        break
    count += 1
    if count >= 3:
        print("Locked out")
        break