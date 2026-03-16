x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
    print(f"x is greater: {x}")
elif y > x:
    print(f"y is greater: {y}")
else:
    print(f"Both x and y are equal: {x} and {y}.")