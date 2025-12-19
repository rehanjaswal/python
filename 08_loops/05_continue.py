# for i in range(1,21):
#     if i == 5:
#         continue        continue means skip this iteration and start the loop from the next one
#     print(i)            used when you wanna skip some values but want the loop to keep running

numbers = [2,-7,7,8,10,-3,-9]
for n in numbers:
    if n<0:
        continue
    print(n)