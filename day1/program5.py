scores = []
strike = []
print("Enter runs scored by each player:")
for i in range(0,3):
    run = int(input())
    scores.append(run)

for i in range(0,3):
    rate = (scores[i]*100)/60
    strike.append(rate)

print("Strike Rates of each player:")
for i in range(0,3):
    print("Player", i+1, ": ", strike[i])

print("Runs scored by each player on playing 60 more balls:")
for i in range(0,3):
    print("Player", i+1, ": ", int((strike[i]*120)/100))

print("Maximum number of sixes each player could have hit:")
for i in range(0,3):
    print("Player", i+1, ": ", int(scores[i]/6))
