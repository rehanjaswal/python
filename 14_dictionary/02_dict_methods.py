student = {"name" : "rehan", "GPA" : 6.7, "football_club" : "Man United", "IPL_team" : "Punjab Kings", "GOAT" : "Rafa Nadal"}

print(student.keys())  
print(student.values())
student.pop("GPA") # removes the desired key-value pair
print(student)
student.clear()  # clears the entire dict
print(student)

