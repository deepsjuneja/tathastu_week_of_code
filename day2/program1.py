num = int(input("Enter a number: "))

if num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

c = 0
for i in range(2,num):
    if num%i == 0:
        c += 1
        break
    
if c == 0:
    print("Number is prime")
else:
    print("Number is not prime")

rev = 0
n = num
while n != 0:
    d = int(n%10)
    rev = int(rev*10+d)
    n = int(n/10)

if num == rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

n1 = num
sum = 0
while n1 != 0:
    d = int(n1%10)
    sum += (d*d*d)
    n1 = int(n1/10)

if num == sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
