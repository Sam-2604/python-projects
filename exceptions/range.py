def main():
    number = int(input("Enter a number: "))
    result = enter(number)
    print("Number:",result)

def enter(x):
    if 1 <= x <= 10:
        return x
    else:
        raise ValueError("Number must be between 1 and 10")
    
main()