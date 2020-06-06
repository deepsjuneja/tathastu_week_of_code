n = int(input("Enter no. of elements in list: "))

List = []
print("Enter elements of list one by one: ")
for i in range(n):
    ele = int(input())
    List.append(ele)

k = int(input("Enter the number k: "))
print("List: ", List)
List = sorted(List)

print("kth smallest element: ", List[k-1])
