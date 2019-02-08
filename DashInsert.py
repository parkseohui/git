#Dash Insert
#입력: 숫자를 입력받기
#출력: 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가한 문자열
a=input("숫자를 입력해주세요")
b=list()
for i in range(len(a)-1):
    b.append(a[i])
    if int(a[i])%2==1 and int(a[i+1])%2==1:
        b.append('-')
    if int(a[i])%2==0 and int(a[i+1])%2==0:
        b.append('*')
b.append(a[i+1])    
print(b)
b = ''.join(str(e) for e in b) #how to list to string
print(b)
