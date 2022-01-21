#https://www.acmicpc.net/problem/5622

#딕셔너리로 만든 후 2:[a,b,c] val에 포함되어 있으면 그 ket로 계산?
#아니면 a:2, b:2 이것처럼 모든 알파벳 일일이?
#아니면 for문 2번이나 3번 돌려?

#dic은 검색이 빠르기때문에 구성해 봤당
import collections
import sys

rule = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
str_list = sys.stdin.readline()
dic_num = collections.defaultdict(str)

for str_word in rule:
    dic_num[rule.index(str_word)+3] = str_word

result = 0
for i in str_list:
    for key, value in dic_num.items():
        if i in value:
            result += key
print(result)

#other
li=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=input()
cnt=0
for i in range(len(word)):
    for j in li:
        if word[i] in j:
            cnt+=li.index(j)+3
print(cnt)




