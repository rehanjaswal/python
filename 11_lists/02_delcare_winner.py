#votes

votes = ["A", "B", "C", "D", "A", "A", "B", "C", "A", "B"] 

# calculate number of votes

a = votes.count("A")    
b = votes.count("B")
c = votes.count("C")
d = votes.count("D")

#merge candidates and votes together by making a list

results = [["A", a], ["B", b], ["C",c], ["D",d]]

# now sort them but in decreasing order (by defualt list.sort sorts in increasing)
results.sort(key=lambda x: x[1], reverse=True)

rank = 1
for candidate in results:
    print(rank,"->",candidate[0],"with",candidate[1],"votes")
    rank+=1