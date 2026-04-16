# Reads students.csv from problem 2, filters 
# only students whose name starts with a letter between A-M, 
# writes them to a new file filtered.csv with the same headers

def main():
    with open("students.csv", "r") as file, open("filtered.csv", "w") as new_file:
        readers = file.readline() 
        new_file.write(readers) 
        for line in file:
            name = line.split(",")[0] 
            if name[0].upper() >= "A" and name[0].upper() <= "M": 
                new_file.write(line)
                
if __name__ == "__main__":
    main()