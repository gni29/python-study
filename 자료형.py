'''
t1 = (10,20,30)

print(t1[0])
del t1

t2 = (10)
t3 = (10,)
t4 = 10,
print(type(t4))

name = ['흥부','콩쥐','놀부','콩쥐']
dupl_name =set()

for i in range(len(name)):
    if name.count(name[i]) > 0 :
        print(name[i])
name_set = set(name)
name_list = list(name_set)
print(name_list.sort())

name = ["1","2","3","2"]
a = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
       a.append(name[i])
name = a
print(name)

dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic.keys():
    print(f'{word}: {dic[word]}')
else :
    print("정의된 단어가 없습니다.")

총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans+=1
print(ans)

name = ['Alice',"Bob","Charlie"]
score = [85,90,95]
grade = {n:s for n,s in zip(name,score)}
print(f'grade : {grade}')
grade['David'] = 80
print(f'David : {grade['David']}')
grade['Alice'] = 88
print(f'modified Alice : {grade['Alice']}')
del grade['Bob']
for k in grade.keys() :
    print(f'{k} : {grade.get(k)}')
'''
