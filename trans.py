#숫자를입력받으면 그에맞는자릿수 출력
'''
num=input("숫자를 입력해주세요")
result=[1]
for i in num:
    result.append(0)
result.pop()

print(str(result),"의 자리수입니다.")
'''
'''
num=input("숫자를입력해주세요.")
result=1

for i in range(len(num)-1):
    result=10*result


print(result)

'''

num=input("숫자를입력해주세요.")
result=[(10**i)*10 for i in range(len(num)-1)]
result.reverse()
for i in range(len(result)-1):
    result.pop()
print(str(result)+'의 자리')

#컴프리핸션을 좋아하는 최모씨의 부탁으로 만들어봤습니다.
