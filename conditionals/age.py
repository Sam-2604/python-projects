age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age < 65:
    print("Adult")
else: 
    print("Senior Citizen")