n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i):
        print(n-i, end="")
    print()

# Output
Enter the number of rows: 5
55555
4444
333
22
1
