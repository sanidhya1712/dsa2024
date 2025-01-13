#Optimized sol
def is_palindrome(string):
    palindrome = True
    i = 0
    j = len(string)-1
    if (len(string)%2 == 0) :
        print("even")
        while (i<j) :
            print(i,"  ",j)
            if (string[i]==string[j]) :               
                i+=1
                j-=1
            else:
                palindrome = False
                break
    else:
        print("odd")
        while (i<=j) :
            print(i,"  ",j)
            if (string[i]==string[j]):             
                 i+=1
                 j-=1
            else:
                 palindrome = False
                 break
    return palindrome
print(is_palindrome('a1a'))