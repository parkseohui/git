#MaxLimitCalculator 클래스이다.
#MaxLimitCalculator 클래스는 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 클래스이다

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value+=val
        if self.value>100:
            self.value=100
      
