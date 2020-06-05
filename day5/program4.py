def Knapsack(wt, val, W, n):
    if W == 0 or n == 0:
        return 0
    
    if wt[n-1] > W:
        return Knapsack(wt, val, W, n-1)
    
    else:
        return max(val[n-1] + Knapsack(wt, val, W-wt[n-1], n-1), Knapsack(wt, val, W, n-1))
        

n = int(input("Enter the no. of elements in arrays: "))

val = []
wt = []

print("Enter values one by one: ")
for i in range(n):
    value = int(input())
    val.append(value)

print("Enter weights one by one: ")
for i in range(n):
    weight = int(input())
    wt.append(weight)

W = int(input("Enter capacity of Knapsack: "))

print("Value of maximum value subset of val[]: ", Knapsack(wt, val, W, n))
