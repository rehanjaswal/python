import math
import requests
# x = int(input("enter a number: "))
# # print("square root of",x,"is",math.sqrt(x))
r = requests.get("https://x.com/rehanjaswal")
# print(r.text)
print(r.status_code)