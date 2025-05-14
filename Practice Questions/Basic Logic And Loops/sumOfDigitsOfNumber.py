n=int(input("Enter a number: "))
sum=0

while n>0:
    lastDigit=n%10
    sum+=lastDigit
    n=n//10
print(sum)
