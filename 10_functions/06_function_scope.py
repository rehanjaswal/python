def multiply(x,y):
    z = 7     # local variable...gets created when function calls itself and gets destoryed when it returns
    return x*y

z = 10 # global variable
print(multiply(2,3))
print(z)