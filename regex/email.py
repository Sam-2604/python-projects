# Asks the user for an email address, uses re.fullmatch to validate it
# — must have characters before @, a domain,
# and a valid extension of 2-3 characters. Print "Valid" or "Invalid"

import re


def main():
    email = input("Enter an email address: ")
    pattern = r"^[\w]+@[\w]+\.\w{2,3}$"

    if re.fullmatch(pattern, email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
