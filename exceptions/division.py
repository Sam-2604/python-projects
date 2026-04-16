def main():
    result = divide()
    print(result)

def divide():
    while True:
        try:
            x = int(input("Enter the numerator: "))
            y = int(input("Enter the denominator: "))
            return x / y
        except ValueError:
            print("Cannot convert input to integer. Please enter valid integers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please try again.")
    
main()   
 