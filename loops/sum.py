total = 0

prices = {"apple": 1.2, 
          "banana": 0.8, 
          "orange": 1.5
          }

for item in prices:
    total += prices[item]

print(f"The total cost is: {total}")