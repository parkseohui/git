#중앙값 구하기
'''
리스트에 있는 숫자들의 중앙값을 구하는 프로그램을 만들어라.
[7, 9, 14] = 9
[24, 31, 35, 49] = 33
[17, 37, 37, 47, 57] = 37

중앙값 : 자료를 작은 값에서부터 크기순으로 나열할 때 중앙에 위치한 값
① 자료의 개수가 홀수이면 가운데 위치한 값이 중앙값이다.
② 자료의 개수가 짝수이면 가운데 위치한 두 값의 평균이 중앙값이다.

'''
list1=list(map(int,input('입력하세요').strip().split()))
n=int(round(len(list1)/2))
list1.sort()
print(list1)
if len(list1)%2==0:
    print((list1[n-1]+list1[n])/2)
if len(list1)%2==1:
    print(list1[n])
