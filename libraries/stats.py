# Imports statistics — ask the user for numbers one per line
# until EOF, store them in a list,
# then print the mean, median, and mode formatted to 2 decimal places.

import statistics


def main():
    number = []
    while True:
        try:
            number.append(float(input("Number: ")))
        except EOFError:
            break

    print(f"Mean: {statistics.mean(number):.2f}")
    print(f"Median: {statistics.median(number):.2f}")
    print(f"Mode: {statistics.mode(number):.2f}")


if __name__ == "__main__":
    main()
