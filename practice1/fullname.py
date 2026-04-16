# Ask the user for a full name in "First Last" format, validate that it contains exactly two words and only letters 
# — if not, reprompt. Output it formatted as "Last, First" in uppercase. 
# Use a function for validation that raises ValueError on invalid input.

def main():
    while True:
        try:
            full_name = input("Enter a full name (First Last): ")
            last, first = validate_full_name(full_name)
            print(f"{last.title()}, {first.upper()}")
            break
        except ValueError as e:
            print(e)

def validate_full_name(name):
    parts = name.split()
    if len(parts) != 2:
        raise ValueError("Invalid input: Please enter exactly two words.")
    
    first, last = parts
    if not (first.isalpha() and last.isalpha()):
        raise ValueError("Invalid input: Names must contain only letters.")
    
    return last, first

main()