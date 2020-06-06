def arrange(List, n):
    for i in range(n-1, 0, -1):
        if List[i] > List[i-1]:
            break
    
    if i == 1 and List[i] <= List[i-1]:
        print("There is no greater number")
        return
    
    ind = i
    small = List[i-1]
    for j in range(i+1, n):
        if small < List[j] and List[j] < List[ind]:
            ind = j
    
    List[ind], List[i-1] = List[i-1], List[ind]

    re_num = 0
    for j in range(i):
        re_num = re_num*10 + List[j]
    
    List = sorted(List[i:])
    for j in range(n-i):
        re_num = re_num*10 + List[j]

    print("Re-arranged number: ", re_num)


num = input("Enter the integer: ")
List = []
for c in num:
    List.append(int(c))
l = len(List)
arrange(List, l)
