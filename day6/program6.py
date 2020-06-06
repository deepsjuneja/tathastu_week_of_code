n = int(input("Enter no. of elements in array: "))

array = []
print("Enter elements of array one by one: ")
for i in range(n):
    ele = int(input())
    array.append(ele)

minele = min(array)
pos = array.index(minele)

sub1 = array[:pos]
sub2 = array[pos + 1:]

sub1_s = sorted(sub1)
sub2_s = sorted(sub2)

c1 = 0
c2 = 0
for i in range(len(sub1)):
    if sub1[i] != sub1_s[i]:
        c1 = -1
        break

for i in range(len(sub2)):
    if sub2[i] != sub2_s[i]:
        c2 = -1
        break

if c1 != -1 and c2 != -1:
    if array[-1] < array[pos-1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
