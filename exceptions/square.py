def main():
    number = input("Enter a number to square: ")
    try:
        result = square(number)
        print("Squared:", result)
    except TypeError as e:
        print(e)

def square(n):
    try:
        n = float(n)
    except ValueError:
        raise TypeError("Not a number")
    return n * n

main()