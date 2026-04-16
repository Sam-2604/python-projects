# This program prompts the user to enter their name and then greets them with a personalized message.

user_input = str(input("Enter your name: "))

def hello(name):
    return "Hello, " + name + "!"

result = hello(user_input)
print(result)
