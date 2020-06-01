n = int(input("Enter the value of n: "))

for i in range(n):
    print("* " * (n-i) + "    " * i + " *" * (n-i))
for i in range(1,n+1): # In the question, the pattern has 2 lines having 2 stars each => loop should start from 1
    print("* " * i + "    " * (n-i) + " *" * i)
