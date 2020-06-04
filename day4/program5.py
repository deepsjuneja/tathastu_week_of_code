n = int(input("Enter the no. of votes: "))
List = []

for i in range(n):
    List.append(input("Enter name of the candidate for whom you want to vote: "))

votes = []
for name in List:
    votes.append((name, List.count(name)))

votes.sort(key=lambda x: x[0], reverse=True)
votes.sort(key=lambda x: x[1])

print("Candidate with maximum votes: ", votes[-1][0])
