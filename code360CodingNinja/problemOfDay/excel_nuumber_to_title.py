# Python program to return title to result 
# of excel sheet. 
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Returns result when we pass title. 
def numberToTitle(num):
    # This process is similar to binary-to- 
    # decimal conversion 
    res = []
    i = 0
    rem = 0
    while num>0:
        rem = num%26
        if rem == 0:
            res.append('Z')
            i+=1
            num = (num//26) -1
        else:
            res.append(chr(rem-1 + ord('A')))
            i+=1
            num= num//26
    res = res[::-1]
    result = ''.join(res)
    return res
 
# Driver function 
print(numberToTitle(74)); 