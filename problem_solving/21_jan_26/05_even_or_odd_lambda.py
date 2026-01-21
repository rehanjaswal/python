x = int(input("enter a number: "))

even_or_odd = lambda x: "even" if x%2 == 0 else "odd"

print(f"{x} is {even_or_odd(x)}")