n = input("Enter any Sentence: ")
count = sum(n.count(vowel) for vowel in "aeiou")
print("Count:", count)