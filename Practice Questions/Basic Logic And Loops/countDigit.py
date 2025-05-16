n=int(input("Enter a number: "))
copyOfNone=n
count=0
if n==0:
    print("Count: 0")
while n > 0:
    lastDigit=n%10
    n=n//10
    count+=1
print(count) 

