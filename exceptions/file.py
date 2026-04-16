def main():
    while True:
        try:
            user_input = input("Enter file name: ")
            result = check_file_extension(user_input)
        except ValueError as e:
            print(e)
        else:
            print(result)
            break

def check_file_extension(file_name):
    if not file_name.endswith(".csv"):
        raise ValueError("Invalid file type")
    return file_name

main()