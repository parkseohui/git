#구글 입사문제 중에서
'''1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
 (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함

'''
count=0
count2=0
for i in range(1,10000):
    str(i)
    if '8' in str(i):
        num=str(i)
        print(num)
        count=count+1
        j=num.count('8')
        count2=count2+j
print('8 이 들어간 숫자는 총',count,'입니다.')
print('8은 총',count2,'개 있습니다.')
