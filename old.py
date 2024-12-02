age = int(input('나이를 숫자로 입력해주세요'))
payment = input('결제 방법을 입력해주세요')
if age < 8 or age > 74 :
    bill = '무료'
elif age < 14 :
    bill = 450
    
elif age < 20 :
    if payment == '카드':
        bill = 720
        
    else:
        bill = 1000
        
elif age < 75 :
    if payment == '카드':
        bill = 1200
    else:
        bill = 1300

print( f'{age}세의 {payment}요금은 {bill}원 입니다.')