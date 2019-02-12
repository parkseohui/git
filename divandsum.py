#10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
#입력:10~1000
#출력: 각숫자를 분해후 더한거
#생각할거 : 1.숫자를 나눠야한다  2.나온숫자를 저장하고 더헤야한다
num=[]
for i in range(10,1001):
    s = list(str(i))
    s='*'.join(s)
    num.append(eval(s))
print(sum(num))

    
