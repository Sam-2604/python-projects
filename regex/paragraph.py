# "Contact us at support@company.com or sales@company.com for help"
# Use `re.findall` to extract all email addresses from the string and print each one

import re


def main():
    text = "Contact us at support@company.com or sales@company.com for help"
    pattern = r"\b[\w\.%+-]+@[\w\.-]+\.[A-Za-z]{2,}\b"

    emails = re.findall(pattern, text)

    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
