#집합만들기
s1=set([1,2,3])
s2=set('hello')

#특징2가지
#•중복을 허용하지 않는다.
#•순서가 없다(Unordered).

#교,차,합 집합 구하기
s1&s2 / s1.intersection(s2) #교
s1|s2 / s1.union(s2) #합
s1-s2 /s1.difference(s2) #차

#집합관련함수들
s1.add() #1개의 값추가
s1.update([4,5,6]) #여러개의 값추가
s1.remove(2) #특정한값 제거
