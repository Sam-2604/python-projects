# Part 3 — Class Methods, Static Methods
# Write a Date class that:

# __init__ takes day, month, year as integers — validate ranges
# @classmethod from_string(cls, date_string) that parses "DD/MM/YYYY" and returns a Date instance
# @staticmethod is_leap_year(year) that returns True if the year is a leap year — rule: divisible by 4, except centuries unless divisible by 400
# __str__ returns "DD Month YYYY" e.g. "15 March 1999"

class Date:
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
        }

    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        return f"{self.day} {self.months[str(self.month)]} {self.year}"
    
    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, value):
        if not 1 <= value <= 31:
            raise ValueError("Invalid day")
        self._day = value
        
    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        if not 1 <= value <= 12:
            raise ValueError("Invalid month")   
        self._month = value
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not 1 <= value <= 2026:
            raise ValueError("Invalid year") 
        self._year = value
        

    @classmethod
    def from_string(cls, date_string):
        day, month, year = date_string.split("/")
        return cls(day, month, year)
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    date1 = Date(15, 3, 1999)
    print(date1)
    
    date2 = Date.from_string("15/03/1999")
    print(date2)
    
    print(f"Is 2000 a leap year? {Date.is_leap_year(2000)}")


if __name__ == "__main__":
    main()