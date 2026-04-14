# Takes this string "I was born on 15 March 1999 in Mumbai"
# — use re.search to extract just the date portion "15 March 1999" using capture groups
# Problem 4 must use capture groups with re.search

import re


def main():
    text = "I was born on 15 March 1999 in Mumbai"
    pattern = r"(\d{1,2} \w+ \d{4})"

    match = re.search(pattern, text)

    if match:
        date = match.group(1)
        print(date)
    else:
        print("No date found.")


if __name__ == "__main__":
    main()
