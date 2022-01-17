# https://www.acmicpc.net/problem/2577

result = [int(input()) for i in range(3)]
b= list(map(int, str(result[0]*result[1]*result[2])))

for i in range(10):
    print(b.count(i))