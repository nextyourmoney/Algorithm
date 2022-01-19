#https://www.acmicpc.net/problem/1546

import sys

N = int(input())
score = list(map(int,sys.stdin.readline().split()))
max_num = max(score)
result = sum([num/max_num*100 for num in score])/N
print(result)

#가장 빠른 코드인데 왜 나는 시간이 매번 다르지
N = int(input())
score = list(map(int,input().split()))
max_num = max(score)
for i in range(N):
    score[i] = score[i]/max_num*100
print(sum(score)/N)



