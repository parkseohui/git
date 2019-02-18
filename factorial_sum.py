#재귀함수를 이용해 합을 구하기
def fact(n):
    if n==0:
        return 0
    else:
        return n+fact(n-1)
n=int(input('어디까지 더해드릴까요?'))
print(fact(n))
