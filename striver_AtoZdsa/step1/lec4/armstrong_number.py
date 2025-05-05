# Mathematical with last remainder
def armstrongNumber(n):
    rev = 0
    orig = n
    while n>0:
        ld = n%10
        rev = rev+ pow(ld ,3)
        n = n//10
    print(rev," ", orig)
    return rev == orig
 
print(armstrongNumber(371))