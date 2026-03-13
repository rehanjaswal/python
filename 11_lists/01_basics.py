# midSemMarks = [90, 95, 88, 64, 78]
# endSemMarks = [82, 89, 69, 98, 85]

# print(midSemMarks)
# print(endSemMarks)

# midSemMarks.append(endSemMarks)
# print(midSemMarks)   # outputs [90, 95, 88, 64, 78, [82, 89, 69, 98, 85]]

# # midSemMarks.append(82, 89, 69, 98, 85) # this will throw an error as append only takes one argument, ive given 5 here.

# endSemMarks.append(2)
# print(endSemMarks)

list = [1, 2, 3, 4, 5, 6, 7]

# list.insert(index, value)  (i, x)
# if (i < len(list)) then insert x at the start of the list
# if (i >= len(list)) then insert x at the end of the list

# list.insert(6, 8)
# print(list)

# listX = [1, 2, 3, 4]
# listX.insert(-2, 67) 
# print(listX)         # [1, 2, 67, 3, 4]

# listX.remove(67)
# print(listX)

# listX.reverse()
# print(listX)


# listY = [67, 69, 105, 115]
# listY.sort()
# print(listY)

list1 = [56, 78, 88, 95]

x = list1.pop()
print(list1)
print(x)         # pop returns the removed value
# without passing an argument, pop removes the last element

y = list1.pop(1)   # pop(index)
print(list1)
print(y)

list2 = [1, 2, 3, 7, 67]
print(list2.pop(1))  # prints 2 and not the resulted list after removing 2, as pop always returns the removed value
