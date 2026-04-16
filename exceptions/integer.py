def main():
    example = convert_to_int("ENTER A NUMBER: ")
    print("Number:", example)

def convert_to_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Cannot be converted to an integer.")
        else:
            return user_input
        
main()