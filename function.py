#내장함수 모음집

#절대값을 반환해줌
abs(-3)

#iterable중 거짓이있으면 false리턴
all([1,2,3,0])

#iterable이 모두거짓일때 false
any(["",0])

#숫자입력하면 아스키문자가 나옴
chr(97)

#객체가 가지고있는 변수나 함수를 보여줌
dir([1,2,3])

#몫과 나머지 반환
divmod(1,2)

#번호와 객체
for i,name in enumerate(list):
    print(i,name)

#실행가능한 문자열을 실행
eval('1+2')

#iterable이 함수에 참일때만 보여줌
def positive(x):
    return x>0

print(list(filter(positive,[1,2,3,-3])))

#16진수로 나타내줌
hex(234)

#8진수로 나타내줌
oct(34)

#어디에 저장되있는가
id(s)

#int(x, radix)로 10 진수로 변환시켜줌
int('3a',16)

#이 인스턴스가 이 클래스의 것인가
isinstance(b,person)

#map(f, iterable)로  map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수이다.
def two_times(x):
    return x*2
list(map(two_times,[1,2,3]))

#그 문자의 아스키값을 보여줌
ord('a')

#반올림
round(3,4)

#입력값을 정렬후 리스트로 돌려줌
sorted([3,4,2])

#zip(*iterable) 계수에따라 분류
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
