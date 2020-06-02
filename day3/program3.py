st = input("Enter a string: ")
s = ""

for x in st:
    if x not in s:
        s+=x

print(s)
