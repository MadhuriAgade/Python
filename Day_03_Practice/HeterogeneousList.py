# Create a heterogeneous list of numbers and names. Split the list from highest number
a = [10, "Sakshi", 25, "Rahul", 5, "Priya", 40, "Amit"]

numbers = []
names = []

for i in a:
    if type(i) == int:
        numbers.append(i)
    else:
        names.append(i)

print("Numbers:", numbers)
print("Names:", names)
print("Highest number:", max(numbers))