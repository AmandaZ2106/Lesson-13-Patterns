n=int(input("Enter the amount of rows in your triangle:"))
for row in range(n):
    for j in range(row+1):
        print("* ", end="")
    print()    