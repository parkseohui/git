#1~1000에서 각 숫자의 개수 구하기
b=''
for i in range(1,1001):
        for x in str(i):
                b=b+x

b=','.join(b)
print("0부터 9까지 각개수")
for i in range(10):
        print(b.count(str(i)))


                
    
    

