n=int(input("Enter the number of rows: "))
num=1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num+=1
    print()

# Output:
# Enter the number of rows: 5
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
