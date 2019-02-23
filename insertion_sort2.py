list1 = [5, 4, 1, 3, 2]
n = len(list1)
n
for i in range(1, n):
    mini=i
    for j in range(i-1, -1, -1):
        if list1[mini]<list1[j]:
            list1[j], list1[mini] = list1[mini], list1[j]
            mini=j

    print(list1)
