file = open("data.txt", "r")

lines = file.readlines()

print("Total lines:", len(lines))
print("2nd line:", lines[1])
print("4th line:", lines[3])

file.close()