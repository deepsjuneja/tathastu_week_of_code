n = int(input("Enter the no. of elements in dictionary: "))
dictionary = dict()

for i in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter the value corresponding to key: "))
    dictionary[key] = value

print("Second largest element: ", list(sorted(dictionary.values()))[-2])
