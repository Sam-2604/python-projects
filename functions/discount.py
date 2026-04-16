x = int(input("Enter price: "))
y = int(input("Enter discount: "))

def disc(price, discount):
    return price * (1-(discount/100))

result = disc(x, y)
print(result)