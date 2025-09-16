string=input("Please enter a string:")
vowels="aeiouAEIOU"
num=0
for letters in string:
    if letters in vowels:
        num+=1
print("Number of vowels in the string are:",num)        

