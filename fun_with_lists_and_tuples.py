lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        if lst[i][1] > lst[j][1]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)
