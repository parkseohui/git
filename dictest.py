#딕셔너리표현하기!!
ha={'나':1 , '너':2 , '우리':3}

for h in ha:
    print(h) #이렇게하면 키값만 나오네!

for h in ha.keys():
    print(h) #위와 똑같군



for h in ha.values():
    print(h) #이건 밸류값만 나오는군



for h in ha.keys():
    print('{}의 숫자는 {}입니다.'.format(h,ha[h])) #키와 밸류
 

for key,value in ha.items():
    print('{}의 숫자는 {}입니다.'.format(key,value)) #키와 밸류
    
