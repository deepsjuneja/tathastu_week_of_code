n = int(input("Enter the no. of strings in array: "))
array = []

print("Enter strings in array one by one: ")
for i in range(n):
    word = input()
    array.append(word)

prefix = array[0]
for i in array:
    if len(i) < len(prefix):
        prefix = i

i = 0
l = len(prefix)
while i < n:
    if prefix not in array[i]:
        prefix = prefix[0:l-1]
        l = l - 1
    else:
        i += 1

print("Largest common prefix: ", prefix)
