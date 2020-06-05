def maxValue(List):
    sum_even = 0
    sum_odd = 0
    for i in range(n):
        if i%2 == 0:
            sum_even += List[i]
        else:
            sum_odd += List[i]

    print("Maximum Value that can be stolen by thief: ", max(sum_even, sum_odd))


n = int(input("Enter the no. of houses: "))

Li = []
print("Enter the value stored in each house: ")
for i in range(n):
    value = int(input())
    Li.append(value)

maxValue(Li)
