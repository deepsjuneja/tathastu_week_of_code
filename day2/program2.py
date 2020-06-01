n = int(input("Enter the limit of Fibonacci Series: "))

t1 = 0
t2 = 1

for i in range(1,n+1):
    print(t1)
    sum = t1+t2
    t1 = t2
    t2 = sum
