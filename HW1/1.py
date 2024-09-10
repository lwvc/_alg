fib = [None]*10000
fib[0] = 0
fib[1] = 1
def power2n(n):
    if n < 0: raise
    if not fib[n] is None: return fib[n]
    fib[n]= power2n(n-1)+power2n(n-1) 
    return fib[n]

print(power2n(60))