# Uses sys.argv to accept a name as a command-line argument — if no argument is provided,
# call sys.exit() with an error message. If provided, print "Hello, [name]".
# Run it as python program.py Samarth.
# Rules:
# Problem 2 must use sys.exit() for error cases

import sys


def main():
    if len(sys.argv) < 2:
        sys.exit(
            "Error: No name provided. Please provide a name as a command-line argument."
        )
    else:
        name = sys.argv[1]
        print(f"Hello, {name}")


if __name__ == "__main__":
    main()
