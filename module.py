'''
import calc_module

print(calc_module.add(1,2))
print(calc_module.sub(1,2))
print(calc_module.div(1,2))
print(calc_module.mul(1,2))


import calc_module as cm

print(cm.add(1,2))

from calc_module import add

print(add(1,2))

calc_module.add() # 안됨


from math import floor, ceil
print(floor(3.141592))
print(ceil(3.141592))


import random

print(random.randint(1,5))
print(random.uniform(1,2))
print(random.random())
print(random.randrange(1,3))
print(random.randrange(1,5,2))

import random

com = random.randint(1,100)
min_v = 1
max_v  = 100
count = 0
score = 100
while True:
    try:
        count += 1
        guess = int(input(f'{count} 번째 도전 '+"숫자 입력(%d ~ %d) : " %(min_v, max_v)))
        
        if guess < 0 or guess > 100 :
            print('입력 범위를 초과했어요')
            count -=1
        elif com == guess :
            print("정답이에요")
            print(f"점수 = {score}")
            exit()
        elif com > guess :
            print("랜덤수보다 작아요")
            min_v = guess
            score -= 10
        elif com < guess : 
            print("랜덤수보다 커요")
            max_v = guess
            score -=10
        if count == 10:
            print('도전 가능 횟수 초과입니다.')
            exit()
    except ValueError:
        print('숫자만 입력가능합니다.')
        count -= 1

import random
lottery = []
for i in range(6):
    a = random.randint(1,45)
    if a not in lottery:
        lottery.append(a)
    else :
        i -= 1
sorted(lottery,reverse= True)
print(f"로또 번호 : {lottery}")

import datetime

now = datetime.datetime.today()

print(now)
print(now.year, now.month)

print(f"{now.hour}시 {now.minute}분 {now.second}초")


import datetime
print('지금까지 몇 일?')
first_day =datetime.date(2024,11,25)

today = datetime.date.today()
print(today)

passedtime = today - first_day
print(f'개강 이후 {passedtime}지났습니다.')

import calendar
calendar.prcal(2024)
calendar.prmonth(2024,12)

import datetime
def get_weekday(yyyy,mm,dd):
    days=['월','화','수','목','금','토','일']
    idx = datetime.date(yyyy,mm,dd).weekday()
    print(f'{yyyy}년 {mm}월 {dd}일 {days[idx]}요일')
get_weekday(2025,1,1)

days = ['월', '화', '수','목','금','토','일']
weekday = datetime.date.today().weekday()
print('오늘은 '+days[weekday]+'요일')
weekday = datetime.date(2025, 12, 25).weekday()
print('크리스마스는 '+days[weekday]+'요일')

import time
start = time.time()
print(time.ctime())

import time

# a = time.time()
# time.sleep(2)
# b = time.time()
# print(b-a)

print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

print(time.ctime())
# print(time.ctime(a))
# print(time.ctime(b))

# 1970년 1월 1일 기준
year = time.time()/(365*24*60*60)
print(year)
day = time.time()/(24*60*60)
print(day)

import time
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행 시간 : {end-start}초")

import sys
print(sys.argv)
args = sys.argv[1:]
print(args)

import sys
args = sys.argv[1:]

total = 0
for i in args :
    total += int(i)
print(total)
'''
import sys
args = sys.argv[1:]
if len(args) != 3:
    print('error')
    sys.exit(0)
if args[0] == 'mul':
    print(int(args[1])*int(args[2]))
elif args[0] == 'add':
    print(int(args[1])+int(args[2]))