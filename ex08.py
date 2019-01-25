#1부터 100까지 출력

result=[i for i in range(1,101)]
print(result)


#학급의 평균 점수
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
result=0
for i in a:
    result=result+i

print(result)
print(result/len(a))

################################
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

#다른방법으로 위의 식을 표현하기
numbers = [1, 2, 3, 4, 5]
result=[n*2 for n in numbers if n%2==1]
print(result)

