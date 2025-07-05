num=int(input("Enter a number: "))
numCopy=num
sum=0
while num>0:
    lastDigit=num%10
    sum+=lastDigit**3
    num=num//10
if sum==numCopy:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

# Output
Enter a number: 35
The number is not an Armstrong number.

Enter a number: 371
The number is an Armstrong number.
