a1 = "man united"
r1 = "liverpool"
a2 = "real madrid"
r2 = "barcelona"
a3 = "chelsea"
r3 = "arsenal"

template1 = (f"my favourite club is {a1} and my rival club is {r1}")
print(template1)                                                        # preferred method, newer method

template2 = ("my favourite club is {} and my rival club is {}")

print(template2.format(a3,r3))

print(ord('A'))
print(chr(65))