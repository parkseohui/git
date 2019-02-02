#1~1000에서 각 숫자의 개수 구하기
b=''
for i in range(1,1001):
        for x in str(i):
                b=b+x

b=','.join(b)
print("0부터 9까지 각개수")
print(b.count('0'))
print(b.count('1'))
print(b.count('2'))
print(b.count('3'))
print(b.count('4'))
print(b.count('5'))
print(b.count('6'))
print(b.count('7'))
print(b.count('8'))
print(b.count('9'))


                
    
    

