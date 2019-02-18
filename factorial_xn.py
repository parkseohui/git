#재귀함수를 이용해서 x의 n승 구하기
def fact(x,n):
    if n==0:
        return 1
    else:
        return x*fact(x,n-1)

print(fact(4,4))
