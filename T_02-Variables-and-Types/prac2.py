# Taken user input for all types of variable

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
weight = float(input("Enter your weight (in kg): "))
weight = str(weight) # Convert weight to string for printing
is_student = input("Are you a student? (True/False): ")


print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Weight:", weight)
print("Is Student:", is_student)

print(f"{name} is {age} years old, {height} meters tall, weighs {weight} kg, and it is {is_student} that he is a student.")
