def Sum(List, size, sum):
    sumList = []
    if size == 1:
        for x in List:
            sumList.append(sum + x)
        return sumList
        
    L2 = list(List)
    for x in List:
        L2.remove(x)
        sumList.extend(Sum(L2, size - 1, sum+x))
    return sumList

def summation(List, size):
    li_new = list(List)

    for i in range(2,size+1):
        li_new.extend(Sum(List,i,0))
    
    num = 1
    while True:
        if num not in li_new:
            print("Least sub-element sum which is not a part of the list: ", num)
            break
        num += 1


n = int(input("Enter number of elements of list: "))
li = []

print("Enter elements of list: ")
for i in range(n):
    word = int(input())
    li.append(word)

print("Original List: ", li)
summation(li,n)
