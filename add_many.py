#여러개의 매개변수를 더하는 함수
def add_many(*args):
    result=0
    for i in args:
        result=result+i
    return result
    
