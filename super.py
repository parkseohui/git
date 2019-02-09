#super() 을 쓰는 클래스
class animals():
    def __init__(self,name):
        self.name=name
        print('내 이름은 {}야'.format(self.name))

    def greet(self):
        print('인사를합니다.')


class human(animals):
    def __init__(self,name,speak):
        super().__init__(name)
        self.speak=speak
        print(speak)
