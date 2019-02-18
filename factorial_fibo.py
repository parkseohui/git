def fibo(n):
    # 재귀함수는 탈출조건이 꼭 필요하다.
    if n == 0 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

print(fibo(5))
