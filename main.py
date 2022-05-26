# Body Mass Index Calculator
# Created by Filip Napiorkowski 2022

# Get the user's input for height and weight
height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")

# Convert the input into float numbers
float_height = float(height)
float_weight = float(weight)

# Calculate the body mass index using the formula
body_mass_index = (float_weight / (float_height / 100) ** 2)

#  Round up the result to the nearest 2 decimal places
print(round(body_mass_index, 2))

# Print out the corresponding result based on the calculated number
if body_mass_index < 18.5:
    print("You are underweight")
elif body_mass_index > 18.5 and body_mass_index < 24.9:
    print("You are normal weight")
elif body_mass_index > 25 and body_mass_index < 29.9:
    print("You are overweight")
else:
    print("You are obese")
