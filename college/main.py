# # `x = 10

# # def change():
# #     global x
# #     x = 7

# # change()
# # print(x)


# # y = 10

# # def outerFunction():
# #     y = 20

# #     def innerFunction():
# #         nonlocal y
# #         y = 30              # changes outerFunction's x to 30, global stays unchanged
# #         print(y)

# #     innerFunction()
# #     print(y)
    

# # outerFunction()
# # print(y)

# def greet(name):
#     return "hello " + name

# result = greet("rehan")
# print(result)



# # slope function

# def slope(x1, y1, x2, y2):
#     if (x1 == x2):
#         return "undefined slope"
#     if (y1 == y2):
#         return 0
#     return (y2 - y1) / (x2 - x1)


# def intercept(x, y, slope):
#     return y - slope * x

# m = slope(3, 4, 5, 6)
# print(m)

# y1 = intercept(3, 4, m)
# print(y1)

# y2 = intercept(5, 6, m)
# print(y2)                        #  y1 and y2 yield same result


# import string

# while True:
#     password = input("enter password: ")

#     if len(password) < 8:
#         print("password is too short. try again")
#         continue

#     has_upper = any(c.isupper() for c in password)
#     has_lower = any(c.islower() for c in password)
#     has_digit = any(c.isdigit() for c in password)
#     has_special = any(c in string.punctuation for c in password)

#     if has_upper and has_lower and has_digit and has_special:
#         print("login successful")
#         break
#     else:
#         print("invalid password. try again")


# def count_vowels(s):
#     count = 0
#     vowels = "aeiouAEIOU"

#     for char in s:
#         if char in vowels:
#             count += 1
    
#     return count

# print(count_vowels("hello world"))    # output: 3 (e,o,o)


# check anagrams

# def check_anagrams(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()

#     if sorted(s1) == sorted(s2):
#         print("the two strings are anagrams")
#     else:
#         print("the two strings are not anagrams")


# check_anagrams("akshay", "rehan")   


# age = 19
# weight = 60.5
# is_student = True
# city = "Jalandhar"
# colors = ["red", "green", "blue"]

# total = age + weight

# info = [str(age), str(weight), str(is_student), str(city)]

# colors.append(total)

# print(f"I am {age} years old, weight {weight} kg, and {"am" if is_student else "am not"} a student. I live in {city}. My favourite colors and a total value are: {colors}.")


# s = "HELLO"

# print(s[1:4])   # s[start:stop] start included, start excluded
# print(s[0:5:2])   # start: stop:step ; start at 0, go till 4 (exclude 4) and jump 2 steps always

# String = "My Computer Course"

# x = slice(9)    # slice(none, 9, none) 
# print(String[x])    # My Computer

# x1=slice(-1,-9)    # start = -1 stop = -9 and step = +1 by default
# print(String[x1])
# #   if start > stop then step must be negative or it'll print an empty string



# Write a program to find the sum of the following series (accept
# values of x and n from user) 1 + x/1! + x2/2! + ………..xn/n!

x = float(input("enter value of x: "))
n = int(input("enter value of n: "))

result = 1
term = 1
for i in range(1, n + 1):
    term = term * x / i
    result = result + term

print("sum of series =", result)