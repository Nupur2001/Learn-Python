num=int(input("Enter a number: "))
countDigit=0
while num>0:
    num=num//10
    countDigit+=1
print("Number of digits in the number is: ",countDigit)
