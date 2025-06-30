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

    # The expression (int)(log10(n)+1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
countDigitNum=int(log10(m))+1
print("Number of digits in the number is: ",countDigitNum)    

Time Complexity: O(log10(n))
