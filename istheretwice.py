#0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가
#각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
#입력: 103192319 같은 숫자여러개
#출력: true or false/"중복있음","중복없음"
#고려할거: 1.숫자를 입력받기 2.같은숫자가 두개이상 있는가?
num=input("숫자를입력하세요")
num1=list(num)
num2=set(num)
if len(num1)!=len(num2):
    print("중복이있습니당.")
else:
    print("중복없음")
    



