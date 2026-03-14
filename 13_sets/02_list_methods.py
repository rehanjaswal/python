s = {55, 76, 53, 48, 86, 99}

s.add(67)  # gets added randomly, anywhere
print(s)
s.remove(55)
print(s)
s.remove(86)
print(s)
# throws an error as 66 isnt present in the set
s.discard(48) # removes the element if its present, if not present it doesnt throw an error
print(s)


#removes a random element
# pop doesnt take an argument/paramter, throws an error        

setX = {89, 5, 7, 9, 77, 86}
x = setX.pop()

print(setX)  # returns the set after removing one arbitrary element
print(x)    # returns the removed element