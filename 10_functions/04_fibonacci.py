# series:   0 1 1 2 3 5 8 ... 
# indexing: 0 1 2 3 4 5 6 ...


def fib(n):
    if (n==0 or n==1):
        return n
    else:
        return fib(n-2) + fib(n-1)
    
print(fib(4))

'''= fib(2) + fib(3) 
= fib(0) + fib(1) + fib(1) + fib(2)
= 0 + 1 + 1 + fib(0) + fib(1)
= 0 + 1 + 1 + 0 + 1
= 3'''