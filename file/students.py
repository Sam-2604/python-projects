# Asks the user for name and house pairs one per line until EOF, 
# writes them to a CSV file called students.csv 
# using csv.DictWriter with headers name and house — then reads it back 
# and prints each row formatted as "Name: [name], House: [house]" 
# sorted alphabetically by name

import csv

with open("students.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writeheader()
    
    while True:
        try:
            name = input("Name: ")
            house = input("House: ")
            writer.writerow({"name": name, "house": house})
        except EOFError:
            break
        
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    students = sorted(reader, key=lambda row: row["name"])
    
    for student in students:
        print(f"Name: {student['name']}, House: {student['house']}")