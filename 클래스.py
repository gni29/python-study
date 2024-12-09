'''
class b :
    pass
b()

class Movie:
    title = 'BossBaby'

movie1 = Movie()
movie2 = Movie()
print(movie1.title)
print(movie2.title)

class Movie:
    name = ''
    def __init__(self):
        print("Hello I'm movie Class.")
    def print_msg(msg):
        print(msg)

    def modify(self,movie):
        self.name = movie
    def print_name(self):
        print(self.name)
movie1 = Movie()
movie2 = Movie()
Movie.print_msg('print 하기')
movie1.modify('프린트하기3')
movie1.print_name()
movie2.modify('프린트하기4')
print(movie1.name)
print("movie2.name",movie2.name)



class Movie:
    count = 0
    def __init__(self,title, audience):
        self.title = title
        self.audience = audience
        Movie.count +=1
    def get_title(self):
        return self.__title
    
movie1 = Movie('파묘',100)
movie2 = Movie('파묘2',200)
print(movie1.count)
print(movie2.count)
print(Movie.count)
print()
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)
print()
Movie.count +=1

class Movie:
    count = 0
    def __init__(self, title, audience):
        self.__title = title
        self._audience = audience
        Movie.count += 1
    
    def get_title(self):
        return self.__title
    
    # def set_title(self,title):
    #     self.__title = title

    def get_audience(self):
        return self._audience

movie1 = Movie("파묘", 100)
# print(movie1.__title)
print(movie1.get_title())
# movie1.__title = "오겜"
# print(movie1.get_title())
# print(movie1.__title)
print(movie1._audience)
print(movie1.get_audience())

class MyAdd:
    __a = 1
    __b = 2
    def set__a(self,a):
        self.__a = a
    def sum(self):
        return self.__a + self.__b        

a = MyAdd()
a.set__a(1)
print(a.sum()) # 3
a.set__a(3)
print(a.sum()) # 5

class Health:
    def __init__(self,name):
        self.__name = name
        self.__hp = 100
    def getName(self):
        return self.__name
    def sethp(self,hp):
        hp = max(hp,0)
        hp = min(hp,100)
        self.__hp = hp
    def gethp(self):
        return "hp :" + str(self.__hp)
    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print(f'{hours}시간 운동하다.')
    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다.")
p1 = Health("나몸짱")
p1.sethp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.getName()} - {p1.gethp()}")

p2 = Health("나약해")
p2.sethp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.getName()} - {p2.gethp()}")

class calculation:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def add(self):
        return self.__a+self.__b
    def sub(self):
        return self.__a -self.__b
    def div(self):
        if self.__b != 0:
            return self.__a/self.__b
        elif self.__b == 0 :
            return None
    def mul(self):
        return self.__a*self.__b

c  = calculation(5,3)
print(f'add : {c.add()}, sub : {c.sub()}, mul : {c.mul()}, div : {c.div()}')
c  = calculation(4,0)
print(f'add : {c.add()}, sub : {c.sub()}, mul : {c.mul()}, div : {c.div()}')
'''
class Employee:
    serial_num = 1000
    def __init__(self,name):
        Employee.serial_num +=1
        self.id = Employee.serial_num
        self.name = name
    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"
e1 = Employee('최사원')
print(e1)
e2 = Employee("안사원")
print(e2)
e3 = Employee('한사원')
print(e3)

employee = [Employee('구름'),Employee('별'),Employee('행성'),Employee('달')]
for i in range(len(employee)):
    print(employee[i])