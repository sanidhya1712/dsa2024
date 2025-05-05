import math 
#  Brute for will be iterate till n and check remainder = 0. Skipping this

# Optimal- Need to check only till square root and add divisors and quotiont
def hcfgcd(n, m):
    count = 0
    gcd = 1
    smallest = min(n,m)
    for i in range(1, smallest+1):
        if(n%i == 0 and m%i == 0):
            gcd = i
    return gcd
 
print(hcfgcd(25, 36))