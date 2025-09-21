pattern = int(input("Enter the size of the pattern: "))
rows = pattern

for row in range(rows):
    for i in range(rows):
        print("*", end="")
    print()
