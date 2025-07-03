num=int(input("Enter a number: "))
numCopy=num
revNumber=0
while num>0:
    digit=num%10
    revNumber=revNumber*10+digit
    num=num//10
print("Reversed number is: ",revNumber)

if revNumber==numCopy:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
