import math 
#  Brute for will be iterate till n and check remainder = 0. Skipping this

# Optimal- Need to check only till square root and add divisors and quotiont
def primeNumber(n):
    count = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if(n%i == 0):
            count+=1
            if n//i!= i:
                count+=1
    return count==2
 
print(primeNumber(25))