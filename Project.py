n = int(input("Enter the amount of rows in your triangle: "))
print("\nLeft-aligned triangle:")
for row in range(n):
    for j in range(row + 1):
        print("* ", end="")
    print()
print("\nRight-aligned (reflection) triangle:")
for row in range(n):
    for space in range(n - row - 1):
        print("  ", end="")   
    for j in range(row + 1):
        print("* ", end="")
    print()