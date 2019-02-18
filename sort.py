list1=[5,2,4,6,1,3]
for i in range(len(list1)-1):
    if list1[i]>list1[i+1]:
        list1[i],list1[i+1]=list1[i+1],list1[i]
    else:
        break

print(list1)
2,5,4,6,1,3
2,4,5,6,1,3
2,4,5,1,6,3
2,4,5,1,3,6
