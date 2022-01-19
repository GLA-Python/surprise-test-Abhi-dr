data = eval(input("Enter the list: "))

result = []

for a in range(len(data)-1):
    result.append(abs(data[a + 1] - data[a]))

check = []

for a, b in zip(result, result[1:]):
    if a < b:
        check.append(True)
    else:
        check.append(False)

print(all(check))

