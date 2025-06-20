n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")  # spaces
    for k in range(2*i+1):
        print("*",end="")  # stars
    print()


for i in range(n):
    for j in range(i):
        print(" ", end="")  # spaces
    for k in range(2 * (n - i) - 1):
        print("*", end="")  # stars
    print()

# Output:
Enter the number of rows: 5
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
