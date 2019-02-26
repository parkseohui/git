#greatest common divisor 최대공약수
def gcd(a,b): #최대공약수를 구하게 해주는 함수
    i=min(a,b) #둘중 더 작은 숫자를 i에 넣는다
    while True: #계속돈다
        if a%i==0 and b%i==0: #a와 b가 i로 나눠떨어지게 되면
            return i #i를 반환하고 멈춘다
        i=i-1 # 빠져나가지 못할경우 i는 한개씩 줄어가면서 a와 b로 나누어떨어지는 i를 찾게된다.

gcd(4,2)
