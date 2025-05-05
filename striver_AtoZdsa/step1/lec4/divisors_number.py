import math 
#  Brute for will be iterate till n and check remainder = 0. Skipping this

# Optimal- Need to check only till square root and add divisors and quotiont
def divisorNumber(n):
    for i in range(1, int(math.sqrt(n)+1)):
        if(n%i == 0):
            print(i)
            print(n//i)
 
print(divisorNumber(371))