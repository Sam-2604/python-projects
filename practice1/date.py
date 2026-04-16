# Ask the user for a date in DD-MM-YYYY format, validate strictly 
# — day between 1-31, month between 1-12, year between 1900-2100, 
# all must be integers — reprompt on any failure. Output it as "Month DD, YYYY" using a month names list.


def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            user_input = input("Enter date(DD-MM-YYYY): ")
            parts = user_input.split("-")
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])
            
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                raise ValueError("Please use DD-MM-YYYY format")
            
            print(f"{months[month - 1]} {day}, {year}")
            break
        
        except ValueError:
            print("Invalid Input")
            
main()
            