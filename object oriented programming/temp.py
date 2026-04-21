# Write a Temperature class that:

# __init__ takes celsius — must be >= -273.15 (absolute zero), raise ValueError if not
# celsius as a @property with a getter and setter — setter enforces the validation
# fahrenheit as a read-only @property that returns the converted value — formula (C × 9/5) + 32
# __str__ returns "[celsius]°C / [fahrenheit]°F" both formatted to 2 decimal places

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius:.2f}°C / {self.fahrenheit:.2f}°F"
    
    @property
    def celsius(self):
        return self._celsius        
    
    @celsius.setter
    def celsius(self, value):
        if value <= -273.15:
            raise ValueError("Value less than absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

def main():
    today = Temperature(-34)
    print(today)


if __name__ == "__main__":
    main()