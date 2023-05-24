from day03.my_oop01 import Animal


class Human(Animal):

    def __init__(self):  # 생성자
        super().__init__()
        self.tools = []
        self.tools.append("반지")
    
    def farming(self, tool):
        self.tools.append(tool)
        
    def __str__(self):  # toString
        res = "";
        for i in self.tools:
            res += i + " "
        return res
    
    
a1 = Human()
print(a1.age)
a1.birthHappy()
print(a1.age)
print(a1)
a1.farming("샷권")
print(a1)
a1.farming("이클립스")
print(a1)
