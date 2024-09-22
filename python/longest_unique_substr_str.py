#Optimized sol
def max_unique_length(str):
    maxLen = 0
    start = 0
    uniChars = {}
    # currentLen = 0
    for i in range(len(str)):
        print(maxLen, i)
        if str[i] in uniChars:
            print("here -",start)
            start = max(start, uniChars[str[i]]+1)
        uniChars[str[i]] = i
        maxLen = max(maxLen, i -start+1)
    return maxLen
print(max_unique_length('pqbrstbuvwvxy'))