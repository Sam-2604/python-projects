# Asks the user for a phone number in format XXX-XXX-XXXX
# — use re.fullmatch to validate.
# Then use re.sub to strip all non-numeric characters and print just the digits e.g. "1234567890"

import re


def main():
    phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")

    if re.fullmatch(r"\d{3}-\d{3}-\d{4}", phone_number):
        digits_only = re.sub(r"\D+", "", phone_number)
        print(f"Digits only: {digits_only}")
    else:
        print("Invalid phone number format. Please use XXX-XXX-XXXX.")


if __name__ == "__main__":
    main()
