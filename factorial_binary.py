#재귀함수를 이용해서 2진법으로 나타내기
def two_binary(n):
    if n<2:
        print(1,end='')
    else:
        two_binary(n//2)
        print(n%2,end='')

two_binary(18)
    
