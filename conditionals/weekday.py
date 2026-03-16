day = input("Enter day: ")
day = day.lower().strip()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    print("Weekday")
else:
    print("Weekend")