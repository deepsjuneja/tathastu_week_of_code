def replaceGreatest(List):
    sub = []
    for i in range(l-1):
        sub = List[i+1:]
        maxnum = max(sub)
        List[i] = maxnum

    print("Updated list: ", List)


l = int(input("Enter the no. of elements in list: "))
Li = []

print("Enter a list of numbers: ")
for i in range(l):
    num = int(input())
    Li.append(num)

print("Original list: ", Li)

replaceGreatest(Li)
