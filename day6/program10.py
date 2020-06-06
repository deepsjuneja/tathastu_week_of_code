k = int(input("Enter the no. of sorted lists: "))

bigList = []
for i in range(k):
    n = int(input("Enter no. of elements in list " + str(i+1) + ": "))
    List = []
    for j in range(n):
        num = int(input("Enter element " + str(j+1) + ": "))
        List.append(num)
    
    bigList = bigList + List

bigList = sorted(bigList)
print("Single sorted list: ",bigList)
