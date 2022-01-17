#https://www.acmicpc.net/problem/2562


num_list = [int(input()) for i in range(9)]
print(max(num_list),num_list.index(max(num_list))+1)