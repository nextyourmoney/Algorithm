#https://www.acmicpc.net/problem/4344
import sys

num = int(input())
score_list = [list(map(int,sys.stdin.readline().rstrip().split())) for i in range(num)]

for score in score_list:
    score_av = sum(score[1:])/score[0]
    under_av = list(filter(lambda x: x > score_av , score[1:]))
    print(f'{len(under_av)/score[0]*100:.3f}%')