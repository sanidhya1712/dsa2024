def largest_odd_substr(str):
    # Check if the string is empty
    if not str:
        return "0"
    # Remove starting zeros
    str = str.lstrip('0')
    # Check if the last character is odd
    if int(str[-1]) % 2 != 0:
        return str
    
    # If the last character is even, find the largest odd substring
    return largest_odd_substr(str[:-1])
def largest_odd_substr2(str):
    # Check if the string is empty
    if not str:
        return "0"
    # Remove starting zeros
    str = str.lstrip('0')
    # Find the last odd digit and return the substring up to that point
    for i in range(len(str)-1, -1, -1):
        if(int(str[i])%2!=0):

            return str[:i+1]
    return "0"
print(largest_odd_substr2("0000214638"))