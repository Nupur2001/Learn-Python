n=int(input("Enter a number: "))
revNum=0
while n>0:
    lastDigit=n%10
    n=n//10
    revNum=(revNum*10)+lastDigit

print(revNum)
