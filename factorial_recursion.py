#재귀함수 팩토리얼 연습

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input('입력'))
print(factorial(num))
