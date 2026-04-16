# Calculate the energy equivalent of a given mass using Einstein's equation E=mc^2 

user_input = int(input("Enter the mass in kilograms: "))

def einstein(mass):
    speed_of_light = 299792458  # Speed of light in meters per second
    energy = mass * (speed_of_light ** 2)
    return energy

result = einstein(user_input) 
print(f"The energy equivalent of {user_input} kg of mass is: {result} joules")
