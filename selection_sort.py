list1=[4,6,1,3,5,2]
n=len(list1)
for i in range(n-1):
     mini=i
     for j in range(i+1,n):
        if list1[mini]>list1[j]:
            mini=j
     list1[mini],list1[i]=list1[i],list1[mini]
            



print(list1)
