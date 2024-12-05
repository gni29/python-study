'''
def fc(x):
    return x**2 + 2*x +1

print(fc(3))


def sayHi():
    print("Hi")
    print("Hi")
    print("Hi")

sayHi()


x = 10

def func2():
    print("func2", x)
    # print(y)

def func():
    x = 20
    y = 11
    print("func",x, y)
    func2()

func()
print("main", x)
# print("main", y)

func2()

def func3(x):
    print("func3", x)

func3(3)



def cal(n,m):
    if n == m :
        return n*m
    else :
        return n+m
print(cal(n=2,m=2))
print(cal(n=2,m=3))


def delivery(price, count):
    if price *count <20000:
        return price* count + 2500
    else :
        return price * count

print(delivery(30000,1))
print(delivery(17500,1))

vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
def check_machine():
    print(vending_machine)
    
def is_drink():
    beverage = input('마시고 싶은 음료? \n')
    if beverage in vending_machine:
        del vending_machine[vending_machine.index(beverage)]
        print(f'{beverage} 드릴게요')
    else :
        print(f'{beverage} 지금은 없네요')
    print(vending_machine)
    return vending_machine

def add_drink():
    beverage = input('추가할 음료? \n')
    vending_machine.append(beverage)
    print(vending_machine)
def remove_drink():
    code ='삭제'
    beverage = input('삭제할 음료?')
    if beverage in vending_machine :
        del vending_machine[vending_machine.index(beverage)]
    else :
        print(f'자판기에 {beverage}가 존재하지 않습니다.')
    print(vending_machine)
    return vending_machine
check_machine()
is_drink()
add_drink()
remove_drink()

import sys
line= sys.stdin.readline
a = int(line())

def stack_fc():
    i = 0
    stack =[]
    while i < a :
        user_input = line().split()
        b = None
        c = None
        try:
            c = user_input[0]  # 첫 번째 값은 반드시 존재
            b = user_input[1]  # 두 번째 값이 있을 경우 할당
        except IndexError:
            pass  # 두 번째 값이 없으면 b는 None 유지
        
        if c == 'push':
            stack.append(int(b))
        elif c == 'pop':
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack.pop())
        elif c == 'size':
            print(len(stack))
        elif c == 'empty':
            if len(stack) == 0:
                print(1)
            else :
                print(0)
        elif c == 'top':
            if stack :
                print(stack[-1])
            else :
                print(-1)
        i+=1
    return stack
stack_fc()
'''
import sys
line= sys.stdin.readline
a = int(line())

stack = []
def stack_match_case():
    i = 0
    while  i < a:
        user_input = line().split()
        b = None
        c = None
        try:
            c = user_input[0]  # 첫 번째 값은 반드시 존재
            b = user_input[1]  # 두 번째 값이 있을 경우 할당
        except IndexError:
            pass  # 두 번째 값이 없으면 b는 None 유지
        match c :
            case 'push' :
                stack.append(int(b))
            case 'pop' :
                if len(stack) == 0 :
                    print(-1)
                else :
                    print(stack.pop())
            case 'size':
                print(len(stack))
            case 'empty':
                if len(stack) == 0:
                    print(1)
                else :
                    print(0)
            case 'top' :
                if stack :
                    print(stack[-1])
                else :
                    print(-1)
        i+=1
stack_match_case()