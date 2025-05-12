n=int(input("Enter a prime number: "))

if n==1:
  print(f'{n} is not a prime number')
if n>0:
    for i in range(2,n):
        if n%i == 0:
            print(f'{n} is not a prime number')
            break
    else:
        print(f'{n} is a prime number')
