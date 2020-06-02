s = input("Enter a string: ")
l = len(s)

for i in range(l-1,-1,-1):
    print(s[i], end="")
