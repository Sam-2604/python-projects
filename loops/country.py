country = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",  
    "Japan": "Tokyo",
    "Pakistan": "Islamabad",
}

x = input("Which country? ")
if x in country:
    print(f"The capital of {x} is {country[x]}.")
else:
    print("Not found.")