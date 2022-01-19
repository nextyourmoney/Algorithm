#https://www.acmicpc.net/problem/8958

#mine
import sys

num = int(input())
OX_list = [list(sys.stdin.readline().rstrip()) for OX in range(num)]

for i in OX_list:
    score = 0
    for c in range(len(i)):
        if i[c] == 'O':
            score += 1
            i[c] = score

        elif i[c] == 'X':
            score = 0
            i[c] = score
    print(sum(i))

# #다른 사람
# N = int(sys.stdin.readline())
# for i in range(N):
#     quiz_result = sys.stdin.readline()
#     accum = 1
#     score = 0
#     for q in quiz_result:
#         if q is 'O':
#             score += accum
#             accum += 1
#         else:
#             accum = 1
#     print(score)
