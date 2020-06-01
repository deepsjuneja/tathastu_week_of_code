n = int(input("Enter the number of rows: "))

k = 2*n

for i in range(k):
    for j in range(k):
        if i == j or j == k-i-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()
