#https://www.acmicpc.net/problem/10818

import sys

num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().strip().split()))
print(min(num_list),max(num_list))
