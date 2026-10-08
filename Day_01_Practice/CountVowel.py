# Write a Python program to count the number of vowels in a given sentence.
n = input("Enter any Sentence: ")
count = sum(n.count(vowel) for vowel in "aeiou")
print("Count:", count)