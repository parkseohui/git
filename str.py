multiline='''
i'm multiline
haha
'''

a="hi"
print(a*100) #much hi

len(a) # 문자열의 길이를 구해줌

#문자열 슬라이싱
a="life is too short, you need python"
b=a[0:4]

#문자열 포맷팅
year=1995
month=9

print("i'm %d %d" % (year,month))

#function
a.count('i') #갯수세기
a.find('i') #위치반환 없으면 -1을 반환
a.index('i') #위치반환
",".join('abcd') #abcd사이에 ,,삽입
a.upper() #대문자로 바꿈
a.lower() #소문자로 바꿈
a.lstrip() #왼쪽공백지우기
a.rstrip() #오른쪽공백지우기
a.strip() #양쪽공백 지우기
a.replace("life", "my life") #대체하기
a.split() #문자열 나누기
a.split(',') #,기준으로 나누기 
