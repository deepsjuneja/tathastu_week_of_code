n = int(input("Enter the no. of elements in dictionary: "))
dictionary = dict()

for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value corresponding to key: "))
    dictionary[key] = value

diction = dict()

for key,value in dictionary.items():
    if value not in diction.values():
        diction[key] = value

print(dictionary)
print(diction)
