st = input("Enter a string: ")

result = []

def permute(data, i, l):
    if(i == l):
        result.append("".join(data))
    else:
        for j in range(i, l):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, l)
            data[i], data[j] = data[j], data[i]

permute(list(st), 0, len(st))

for x in result:
    print(x)
