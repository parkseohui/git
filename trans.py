#숫자를입력받으면 그에맞는자릿수 출력
num=input("숫자를 입력해주세요")
result=[1]
for i in num:
    result.append(0)
result.pop()

print(str(result),"의 자리수입니다.")
