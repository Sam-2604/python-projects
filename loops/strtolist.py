str1 = "hello, world, python, code, learn"
words = str1.split(", ")
capitalized_list = []

for word in words:
    capitalized_list.append(word.title())

print(" | ".join(capitalized_list))