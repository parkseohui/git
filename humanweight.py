#먹고 걷는 인간 클래스
class Human():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def __str__(self):
        return "{}는 {}kg".format(self.name,self.weight)

    def walk(self):
        self.weight-=1
        print('걸었기 때문에 1키로 빠져서 {}입니다.'.format(self.weight))

    def eat(self):
        self.weight+=2
        print('먹었기 때문에 2키로 쪄서 {}입니다.'.format(self.weight))
              
person=Human('seohui',42)
