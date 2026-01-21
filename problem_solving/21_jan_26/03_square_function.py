# x = int(input("enter a number: "))
# # print("sqaure =",x*x)
# square = lambda x: x*x
# print("square =",square(x))

def square (x):
    return x*x

x = int(input("enter a number: "))
# print("square of",x,"is",square(x))
print(f"square of {x} is {square(x)}")

