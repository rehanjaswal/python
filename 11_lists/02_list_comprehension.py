# write table of 7
# rookie method: 
table = []

for i in range (1, 11) :
    table.append(7 * i)

print(table)

# veteran method

tableVeteran = [7 * i for i in range (1, 11)]
print(tableVeteran)


sqaured = [x ** 2 for x in range (10)]  # sqaures of 0, 1, 2, 3...,9
print(sqaured)

evens = [x for x in range (1, 21) if x % 2 == 0]
print(evens)

alternateSign = [x if x % 2 == 0 else -x for x in range (1, 11)]
print(alternateSign)

words = ["wanker", "gay", "shite"]
upper = [w.upper() for w in words]
print(upper)

moreWords = ['apple', 'banana', 'pineapple']
firstLetter = [l[0] for l in moreWords]
print(firstLetter)


# list comprehension with functions example

def cube(x):
    return x ** 3

cubes = [cube(x) for x in range (11)]
print(cubes)
