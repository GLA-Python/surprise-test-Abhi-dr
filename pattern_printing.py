def print_pattern(user):
    data = []
    a = 0
    while a < len(user):
        count = 1
        while a + 1 < len(user) and user[a] == user[a + 1]:
            count += 1
            a += 1
        data.append(str(count) + user[a])
        a += 1
    return ''.join(data)


output = 1
n = int(input("Enter the number: "))
for i in range(n):
    print(output)
    output = print_pattern(str(output))
