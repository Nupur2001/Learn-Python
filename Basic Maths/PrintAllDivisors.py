num=int(input("Enter a number: "))
divisors=[]
for i in range(1,num+1):
    if num% i==0:
        divisors.append(str(i))
print("The divisors of", num, "are:", ", ".join(divisors))

# Output
Enter a number: 36
The divisors of 36 are: 1, 2, 3, 4, 6, 9, 12, 18, 36
