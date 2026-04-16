# Uses sys.argv to accept a filename as argument, checks if it ends in .py — if not, sys.exit() with a message.
# If yes, print "Valid Python file: [filename]".
# Handle the case where no argument is given separately.

import sys


def main():
    if len(sys.argv) < 2:
        sys.exit(
            "Error: No filename provided. Please provide a filename as a command-line argument."
        )
    else:
        filename = sys.argv[1]
        if filename.endswith(".py"):
            print(f"Valid Python file: {filename}")
        else:
            sys.exit(f"Error: Invalid file type. '{filename}' is not a Python file.")


if __name__ == "__main__":
    main()
