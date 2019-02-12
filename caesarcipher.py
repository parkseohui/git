#시저 암호
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
que=input("원하시는 글자를 입력해주세요")
n=int(input('칸을 입력해주세요'))
result=list()
for i in range(len(que)):
    result.append(list1[list1.index(que[i])+n])

result=''.join(str(e) for e in result)
print(result)

