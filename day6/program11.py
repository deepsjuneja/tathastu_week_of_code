n = int(input("Enter no. of elements in the list: "))

List = []
print("Enter elements of the list one by one: ")
for i in range(n):
    ele = int(input())
    List.append(ele)

List = sorted(List)

pro = 1
for i in range(n-3,n):
    pro *= List[i]

print("Product of the 3 largest elements of list: ", pro)
