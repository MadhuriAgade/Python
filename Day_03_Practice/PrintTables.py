#Print tables of all odd numbers from 1 to 10

for i in range(1, 10, 2):
    j = 1
    while j <= 10:
        print(i, "*", j, "=", i * j)
        j += 1
    print()