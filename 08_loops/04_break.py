# for i in range (1,11):
#     if (i==5):
#         break
#     print(i)

while True:              # infinite loop used cuz idk how many attempts the user gonna take to enter the  right fucking passcode
    passcode = input("enter passcode: ")
    if passcode == "admin123":
        print("access granted")
    else:
        print("access not granted")
        break
