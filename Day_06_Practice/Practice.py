# Find the sum of all numbers in a list
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)


# Count the number of vowels in a string

string = "programming"
count = 0
for char in string:
    if char in "aeiou":
        count = count + 1
print(count)



# Find the largest number in a list

numbers = [12, 45, 23, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)


# Reverse a string

string = "python"
reverse = string[::-1]
print(reverse)


# Replace every occurrence of a character in a string

string = "banana"
new_string = string.replace("a", "x")
print(new_string)
