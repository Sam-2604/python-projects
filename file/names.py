# Creates a text file called names.txt, writes 5 names to it one per line, 
# then reads it back and prints each name with its line number — e.g. "1. Samarth"

with open("names.txt", "w") as file:
    file.write("Samarth\n")
    file.write("Kabir\n")
    file.write("Jaggu\n")
    file.write("Gooney\n")
    file.write("Sheep\n")
    
with open("names.txt", "r") as file:
    lines = file.readlines()
    number = 0
    for name in lines:
        number += 1
        print(f"{number}. {name.strip()}")