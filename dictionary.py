#딕셔너리
a=dict()
a.keys() #키값들을 반환해줌
list(a.keys()) #3.0버전 이후 리스트형으로 키값반환
a.values() #value 값을 반환해줌
a.items() #쌍을 반환해줌
a.clear() #쌍을 모두 지움
a.get('name') #키값으로 value얻기
a.get('what','none') #원하는값이 없을경우 none을 출력하도록함

#해당 키가 딕셔너리에 있는지 조사하기
'name' in a
