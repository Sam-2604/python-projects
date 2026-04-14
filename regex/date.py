# Asks the user for a date in MM/DD/YYYY format,
# uses re.fullmatch with capture groups
# to extract month, day, year separately and print each on its own line
# Problem 3 must use capture groups with re.fullmatch


import re


def main():
    date = input("Enter a date in MM/DD/YYYY format: ")
    pattern = r"(\d{2})/(\d{2})/(\d{4})"
    match = re.fullmatch(pattern, date)

    if match:
        month, day, year = match.groups()
        print(f"Month: {month}")
        print(f"Day: {day}")
        print(f"Year: {year}")
    else:
        print("Invalid date format. Please enter in MM/DD/YYYY format.")


if __name__ == "__main__":
    main()
