n=int(input("Enter a number: "))
copyOfN=n
revNum=0
while n>0:
    lastDigit=n%10
    n=n//10
    revNum=(revNum*10)+lastDigit

if copyOfN==revNum:
    print(f'{copyOfN} is a palindrome')
else:
    print(f'{copyOfN} is not a palindrome')