a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swapping:\na = ",a, "\nb = ",b)

a = a+b
b = a-b
a = a-b

print("After swapping:\na = ",a, "\nb = ",b)
