#2진법으로 자연수 나타내기
num=int(input("숫자를 입력하세요"))
num2=num
result=list()
c=0
while True:
    num=num//2
    c=c+1
    if num==0 or num==1:
        break
    
print(c+1,'개의 공간생성')

for i in range(c+1):
    result.append(num2%2)
    num2=num2//2

result=''.join(str(e) for e in result)    
print(result)

