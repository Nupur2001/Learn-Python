# Time Complexity: O(n)
# Space Complexity: O(n)

n=int(input("Enter a number: "))
divisors=[]
for i in range(1,n+1):
    if n% i==0:
        divisors.append(str(i))
print("The divisors of", n, "are:", ", ".join(divisors))

# Output
Enter a number: 36
The divisors of 36 are: 1, 2, 3, 4, 6, 9, 12, 18, 36

from math import isqrt   # Use isqrt() to get integer square root safely
# Time Complexity: O(√n log √n)
# Space Complexity: O(√n)

num=int(input("Enter a number: "))
divisors=[]
for i in range(1,isqrt(num)+1):
    if num % i == 0:
        divisors.append(str(i))
        if num/i !=i:  
            divisors.append(str(num // i))
divisors.sort()
divisorsStr=[str(d) for d in divisors]
print("The divisors of", num, "are:", ", ".join(divisorsStr))

# Output
Enter a number: 26
The divisors of 26 are: 1, 13, 2, 26
Enter a number: 36
The divisors of 36 are: 1, 12, 18, 2, 3, 36, 4, 6, 9


