'''
## 1-1
n = int(input())
a = [i for i in range(1,n+1)]
print(a)
## 1-2
print(a[1::2])    
print(a[0::2])

## 2
vending_machine = ['게토레이','레쓰비','생수','이프로']
beverage = input('마시고 싶은 음료?')
if beverage in vending_machine:
    print(f'{beverage} 드릴게요')
else :
    print(f'{beverage} 지금은 없네요')
'''
## 3

vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
print(f'남은 음료 :{vending_machine}')
user = input('사용자 종류를 입력하세요 \n 1. 소비자 \n 2. 주인 \n')
if user == '1' :
    beverage = input('마시고 싶은 음료? \n')
    if beverage in vending_machine:
        del vending_machine[vending_machine.index(beverage)]
        print(f'{beverage} 드릴게요')
    else :
        print(f'{beverage} 지금은 없네요')
elif user == '2' :
    check = input('할 일 선택 \n 1. 추가 \n  2. 삭제 \n')
    if check == '2' :
        code ='삭제'
        beverage = input('삭제할 음료?')
        if beverage in vending_machine :
            del vending_machine[vending_machine.index(beverage)]
        else :
            print(f'자판기에 {beverage}가 존재하지 않습니다.')
            exit()
    elif check == '1' :
        code = '추가'
        beverage = input('추가할 음료? \n')
        vending_machine.append(beverage)
    else :
        print('잘못된 값입니다.')
        exit()

    print(f'{code} 완료. \n 남은 음료수 {sorted(vending_machine)}')
    
else :
    print('해당 사용자 번호는 존재하지 않습니다.')
    exit()