n=int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(n-i):
        print("*",end="")
    print()

n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(0,n-i-1):
        print(" ")
    for k in range(0, (2*i)+1):
        print("*")
    print()

# Output
Enter the number of rows: 4
****
***
**
*
