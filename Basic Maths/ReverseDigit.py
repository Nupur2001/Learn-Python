num=int(input("Enter a number: "))
reverseNumber=0
while num>0:
    digit=num%10
    reverseNumber=reverseNumber*10+digit
    num=num//10
print("Reversed number is: ",reverseNumber)

# Output:
Enter a number: 9877
Reversed number is:  7789
