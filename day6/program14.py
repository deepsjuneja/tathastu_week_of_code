n = int(input("Enter the no. of rows and columns: "))

A = []
print("Enter elements one by one: ")
for i in range(n):
    matrix = []
    for j in range(n):
        matrix.append(int(input()))
    A.append(matrix)

print("Original Matrix: ")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()

for i in range(n):
    for j in range(i,n-i-1):
        temp = A[i][j]
        A[i][j] = A[n-j-1][i]
        A[n-j-1][i] = A[n-i-1][n-j-1]
        A[n-i-1][n-j-1] = A[j][n-i-1]
        A[j][n-i-1] = temp

print("Rotated Matrix: ")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
