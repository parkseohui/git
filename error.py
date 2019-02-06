#에러의 이름을 모를때 처리하는 try except문
try:
    a=3/0
except Exception as ex:
    print('에러가 발생했습니다.',ex)
