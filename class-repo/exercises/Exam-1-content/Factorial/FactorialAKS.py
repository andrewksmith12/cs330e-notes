def factorial(n):
    if n <= 1:
        return 1
    return n * factorial((n-1))
def factorial_while(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n-1
    return result
def factorial_for(n):
    result = 1
    for i in range(n,1,-1):
        result = result * i
    return result

