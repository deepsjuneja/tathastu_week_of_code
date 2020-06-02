n1 = int(input("Enter number of elements in first list: "))
n2 = int(input("Enter number of elements in second list: "))

li1 = []
li2 = []

print("Enter elements of first list: ")
for i in range(n1):
    word = input()
    li1.append(word)

print("Enter elements of second list: ")
for i in range(n2):
    word = input()
    li2.append(word)

print("List 1: ", li1)
print("List 2: ", li2)

print("Elements common to both lists are: ")

c = 0
for x in li1:
    if x in li2:
        print(x)
        c+=1

if c == 0:
    print("NONE ")
