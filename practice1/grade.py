# Build a simple student grade tracker 
# — keep asking for "Name Score" pairs one per line until EOF. 
# Store in a dictionary. 
# On EOF print each student and their grade letter 
# (A: 90+, B: 80+, C: 70+, D: 60+, F: below 60) sorted alphabetically by name.

def main():
    students = {}
    while True:
        try:
            line = input().strip()
            name, score = line.split()
            score = grade(score)
            students[name] = score  

        except EOFError:
            for name in sorted(students.keys()):    
                print(f"{name} {students[name]}")
            break
        
        except ValueError:
            print("Invalid input. Please enter in the format 'Name Score'.")

def grade(x):
    x = float(x)
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'    
    
main()