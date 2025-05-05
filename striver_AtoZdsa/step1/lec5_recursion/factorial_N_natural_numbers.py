def factorialNNaturalNumber(n):
    if n==1: 
        return 1
    return n * factorialNNaturalNumber(n-1)
print(factorialNNaturalNumber(3))