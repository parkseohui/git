a=list()
a=input("숫자를 입력하세요:")
b=a.split(',')

result=0
for i in b:
    result=result+int(i)

print(result)
