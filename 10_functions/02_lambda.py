cube = (lambda x: x*x*x)
sum = lambda a,b: a + b

# print(cube(3))
# print(sum(2,3))

x = int(input("enter the number whose cube you wanna find: "))
a = int(input("for addition, enter first number: "))
b = int(input("for addition, enter second number: "))

print("cube of",x,"is",cube(3))
print("sum of",a,"and",b,"is",sum(a, b))  
