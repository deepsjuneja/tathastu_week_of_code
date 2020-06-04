n = int(input("Enter the no. of words in dictionary: "))
diction = []

print("Enter elements in dictionary: ")
for i in range(n):
    diction.append(input())

n = int(input("Enter the no. of words in characyer array: "))
array = []

print("Enter elements in array: ")
for i in range(n):
    array.append(input())

result = []

for word in diction:
    if set(word).issubset(set(array)):
        result.append(word)

for i in result:
    print(i, end=",")
