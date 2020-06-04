nList = int(input("Enter the no. of tuples in list: "))
nTuple = int(input("Enter the no. of elements in each tuple: "))

List = []
for i in range(nList):
    print("Enter the elements in tuple", i+1, "one by one: ")
    Tuple = ()
    for j in range(nTuple):
        a = int(input())
        Tuple = Tuple + (a, )
    List.append(Tuple)

num = int(input("Enter the index by which you want the tuple list to be sorted: "))

for i in range(nList):
    for j in range(nList - i - 1):
        if List[j][num] > List[j+1][num]:
            temp = List[j]
            List[j] = List[j+1]
            List[j+1] = temp
        
print("Sorted Tuple List: ", List)
