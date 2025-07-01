n=int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range (i+1):
        print(chr(j+65), end="")
    print()

# Output:
Enter the number of rows: 5
A
AB
ABC
ABCD
ABCDE
