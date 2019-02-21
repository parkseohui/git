#버블정렬
list1=[1,10,5,8,7,6,4,3,2,9]
n=len(list1)-1
for j in range(n):
    for i in range(n-j):
        if list1[i]>list1[i+1]:
            list1[i+1],list1[i]=list1[i],list1[i+1]
            print(list1)

print(list1)
