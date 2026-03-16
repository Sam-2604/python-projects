x = float(input("Enter number of kms: "))

def mile(kms):
    return round(float(kms * 0.621371), 2)

result = mile(x)
print(f"{x} km is {result} miles.")