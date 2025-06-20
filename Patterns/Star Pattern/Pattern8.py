n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()

for i in range(0,n):
    for j in range(n-i):
        print("*",end="")
    print()

