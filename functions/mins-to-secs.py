x = int(input("Enter number of minutes: "))

def seconds(mins):
    secs = mins * 60
    return secs

result = seconds(x)
print(f"{x} minutes is {result} seconds.")