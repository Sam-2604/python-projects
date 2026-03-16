x = int(input("What's the temperature in Fahrenheit?: ")) 

def farhenheit_converter(F): 
    C = (F - 32) * 5/9
    return C

result = farhenheit_converter(x)
print(result)