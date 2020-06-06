import math

def perfSq(num):
    root = int(math.sqrt(num))
    return root*root == num


def fib(num):
    r1 = perfSq(5 * num * num + 4)
    r2 = perfSq(5 * num * num - 4)
    return r1 or r2


n = int(input("Enter no. of elements in array: "))

array = []
print("Enter elements of array one by one: ")
for i in range(n):
    ele = int(input())
    array.append(ele)

print(array)

sum = 0
for i in array:
    if fib(i):
        sum += i

print("Required Sum: ", sum)

if fib(sum):
    print("Sum belongs to Fibonacci Series")
else:
    print("Sum does not belong to Fibonacci Series")
