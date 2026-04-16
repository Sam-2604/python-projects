names = []
new_names = []

for i in range(5):
    user_input = input("Enter a name: ")
    names.append(user_input)

for name in names:
    if len(name) > (4):
        new_names.append(name)
        
print(new_names)