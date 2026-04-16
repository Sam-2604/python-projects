# Imports random and creates a function that takes a list of names and
# returns a randomly selected one — call it 3 times and print each result.
# Then use random.shuffle() on the list and print the shuffled version.

import random


def main():
    names = ["Sam", "Jaggu", "Baigir", "Gooney", "Balgam", "Sheep", "Randi"]
    for _ in range(3):
        print(random.choice(names))

    random.shuffle(names)
    print(f"Shuffled names: {names}")


if __name__ == "__main__":
    main()
