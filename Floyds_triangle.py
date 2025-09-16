number=1
print("Floyd's triangle")
rows=int(input("Enter the amount of rows:"))
for num in range(1,rows+1):
    for i in range(1,num+1):
        print(number,end=" ")
        number=number+1
    print()   

    