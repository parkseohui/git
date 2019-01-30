#3과 5의 배수의합

#입력: 1~1000
#출력: 3과 5의배수의합
#think 1.3과5의배수구하기 2.3과5가겹칠땐?
result=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result=result+i


print(result)
        
    
    
