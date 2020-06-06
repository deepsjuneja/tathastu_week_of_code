def spiral(array, m, n, i, j):
    if i >= m or j >= n:
        return
    
    for x in range(i,n):
        print(array[i][x], end=" ")

    for x in range(i+1,m):
        print(array[x][n-1], end=" ")

    if m-1 != i:
        for x in range(n-2,j-1,-1):
            print(array[m-1][x], end=" ")

    if n-1 != j:
        for x in range(m-2,i,-1):
            print(array[x][j], end=" ")

    spiral(array, m-1, n-1, i+1, j+1)


m = int(input("Enter the no. of rows: "))
n = int(input("Enter the no. of columns: "))

A = []
print("Enter elements one by one: ")
for i in range(m):
    matrix = []
    for j in range(n):
        matrix.append(int(input()))
    A.append(matrix)

print("Original Matrix: ")
for i in range(m):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

spiral(A, m, n, 0, 0)
