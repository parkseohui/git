# A학급 학생의 점수를 나타내는 리스트.
#다음 리스트에서 50점 이상의 점수들의 총합
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
num=0
result=0
while num<len(a):
    if a[num]>=50:
        result=result+a[num]
    num=num+1
    
print(result)

#다른방법
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result=0
while a:
    mark=a.pop()
    if mark>=50:
        result=result+mark


print(result)
