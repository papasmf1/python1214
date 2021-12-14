# class1.py 
# 클래스를 정의
class Person:
    #생성자(초기화)메서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p1.name = "전우치"
p2 = Person() 

p1.print()
p2.print() 

#런타임(실행시간에 추가)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30
print(p1.age)
#print(p2.age)




