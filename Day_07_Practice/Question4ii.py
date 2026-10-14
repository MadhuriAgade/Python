file = open("data.txt", "r")

content = file.read()
words = content.split()

unique_words = set(words)
print("Unique words:", unique_words)

file.close()