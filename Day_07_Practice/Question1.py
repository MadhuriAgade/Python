file = open("data.txt", "r")
content = file.read()
count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count = count + 1
print(content)                
print("Vowel in the file:", count)
file.close()