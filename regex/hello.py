# Takes this string "    Hello, World!    "
# — use re.sub to remove all leading and trailing whitespace without using .strip().
# Then take "hello world foo bar" and
# use re.sub to capitalise the first letter of every word without using .title()
# No .strip() or .title() in problem 5

import re


def main():
    string1 = "    Hello, World!    "
    string2 = "hello world foo bar"

    cleaned_string1 = re.sub(r"^\s+|\s+$", "", string1)
    print(cleaned_string1)

    capitalised_string2 = re.sub(
        r"\b\w", lambda match: match.group(0).upper(), string2
    )
    print(capitalised_string2)


if __name__ == "__main__":
    main()
