#평균 구하기
'''리스트에 있는 숫자들의 평균을 구하는 프로그램을 만들어라.
[4, 6, 8] = 6
[11, 17, 20, 24] = 18
[26, 33, 45, 51, 60] = 43'''
num=list(map(int,input('입력하세요').strip().split(',')))
print(num)
print(sum(list(num))/len(num))
    
