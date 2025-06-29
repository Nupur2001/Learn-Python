n=int(input("Enter the number of rows: "))
space= 2*(n-1)
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    for j in range(space):
        print(" ", end="")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()
    space -= 2

# Output
Enter the number of rows: 5
1         1 
1 2       2 1 
1 2 3     3 2 1 
1 2 3 4   4 3 2 1 
1 2 3 4 5 5 4 3 2 1 
