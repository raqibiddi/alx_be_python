pattern = int(input("Enter the size of the pattern: "))
rows = pattern
row = 0

while row < rows:
    i = 0
    while i < rows:
        print("*", end="")
        i += 1
    print()
    row += 1