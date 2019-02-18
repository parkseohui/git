#Every Other Digit
'''
모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6
'''
#조건 짝수번째 인덱스여야한다. 그리고 숫자여야한다.
#num=input('입력하세요')
num='a1b2cde3~g45hi6'
print(len(num))
count=0
for i in num:
    count=count+1
    if count%2==0 and i.isdigit():
        print(i,count)
        num=num.replace(num[count-1],'*')
print(num)
