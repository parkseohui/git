#단순한 나만의 오류 예제
class myexception(Exception):
    print('오류입니다 고갱님')


try:
    if 'w' not in ['a']:
        raise myexception
except myexception:
    '''이런'''
