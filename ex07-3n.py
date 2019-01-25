#1부터 1000까지의 자연수 중 3의 배수의 합
num=0
result=0
while num<=1000:
    num=num+1
    if num%3==0:
        result=result+num
        print(num)


print("3의 배수의 합은 : %d입니다." % result)
    
