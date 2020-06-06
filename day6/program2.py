n = int(input("Enter no. of elements in unsorted list: "))

List = []
print("Enter elements of list one by one: ")
for i in range(n):
    ele = int(input())
    List.append(ele)

print("Sorted List: ", List)
print("Unsorted List: ", sorted(List))
