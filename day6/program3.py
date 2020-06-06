n = int(input("Enter no. of elements in unsorted list: "))

List = []
print("Enter elements of list one by one: ")
for i in range(n):
    ele = int(input())
    List.append(ele)

k = 1
j = 0
while(j < n):
    if k not in List:
        break
    else:
        k += 1
    j += 1

print("Smallest positive no. missing from the list: ", k)
