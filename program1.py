n = int(input("Enter no. of elements in Tuple: "))

tup = ()
print("Enter elements of tuple one by one: ")
for i in range(n):
    a = input()
    tup = tup + (a ,)

ele = input("Enter the element to be searched: ")

c=0
for i in range(n):
    if tup[i] == ele:
        c+=1
print("Tuple: ", tup)
print(ele, "occurs", c, "time(s)")
