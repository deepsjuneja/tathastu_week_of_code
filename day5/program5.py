def arrange(array):
    odd = []
    even = []

    for i in array:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)

    array = sorted(odd, reverse=True) + sorted(even)
    print("Re-arranged array: ", array)


n = int(input("Enter no. of elements in array: "))

Array = []
print("Enter the elements of array one by one: ")
for i in range(n):
    ele = int(input())
    Array.append(ele)

print("Original array: ", Array)
arrange(Array)
