def triplet(List):
    n = len(List)
    for i in range(n-2):
        j = i+1
        k = n-1

        while j < k:
            sum = float(List[i] + List[j] + List[k])
            if sum > 1 and sum < 2:
                print("Triplet exists!\nTriplet elements: ", List[i], ",", List[j], ",", List[k])
                return True
            elif sum < 1:
                j += 1
            else:
                k -= 1
    
    return False


n = int(input("Enter no. of elements in list: "))

List = []
print("Enter elements of list one by one: ")
for i in range(n):
    ele = float(input())
    List.append(ele)

List = sorted(List)
if triplet(List) is False:
    print("Triplet does not exist")
