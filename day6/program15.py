def left(sub, num):
    for i in sub:
        if i >= num:
            return False
    return True

def right(sub, num):
    for i in sub:
        if i <= num:
            return False
    return True


n = int(input("Enter no. of elements in unsorted list: "))

List = []
print("Enter elements of list one by one: ")
for i in range(n):
    ele = int(input())
    List.append(ele)

c = 0
for i in range(1,n):
    sub1 = List[:i]
    sub2 = List[i+1:]

    if left(sub1, List[i]) and right(sub2, List[i]):
        c = -1
        print("Required smallest element: ", List[i])
        break

if c != -1:
    print("No such element found")
