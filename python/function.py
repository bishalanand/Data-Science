import math

# Example of using map to uppercase a list of strings (commented out)
# list1 = ["heelo", "kaise", "ho", "achah"]
# list2 = list(map(lambda x: x.upper(), list1))
# print(list2)

radii = []
n = 6

for i in range(n):
    a = int(input(f"Enter radius {i+1}: "))  # More descriptive prompt
    radii.append(a)

areas = list(map(lambda x: math.pi * x**2, radii))
print("Areas:", areas)
