n = int(input("Enter number of elements of list: "))
li = []

print("Enter elements of list: ")
for i in range(n):
    word = input()
    li.append(word)

print("Original List: ", li)

li_new = []

for x in li:
    if x not in li_new:
        li_new.append(x)

print("Updated list: ", li_new)
