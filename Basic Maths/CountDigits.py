# Brute Force Method to Count Digits in a Number
# This method repeatedly divides the number by 10 until it becomes 0,
# counting how many times this division occurs, which gives the number of digits.
num=int(input("Enter a number: "))
countDigit=0
while num>0:
    num=num//10
    countDigit+=1
print("Number of digits in the number is: ",countDigit)

# Optimized Method to Count Digits in a Number
# The second method uses the logarithm to count the digits in a number.
# It is more efficient for large numbers compared to the first method.
from math import log10
m=int(input("Enter a number: "))
countDigitNum=int(log10(m))+1
print("Number of digits in the number is: ",countDigitNum)    

Time Complexity: O(log10(n))
