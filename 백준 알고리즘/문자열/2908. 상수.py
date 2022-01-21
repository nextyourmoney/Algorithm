#https://www.acmicpc.net/problem/2908

#쓰래기 같은 내 코드^^ #괜히 어렵게 해보겠다고 지랄 햅ㅆ네
import sys

nums = list(sys.stdin.readline().split())
for i in range(2):
    left, right = 0, 2  # 투 포인터 사용 (문제에 3자리수로 정의 되어있으므로)
    list_str = list(nums[i])

    while left < right:
        list_str[left], list_str[right] = list_str[right], list_str[left]
        left += 1
        right -= 1

    nums[i] = int(''.join(list_str))
print(max(list(map(int, nums))))

#다른 분들
a, b =input().split()

def reading(k):
    k = k[::-1]
    return int(k)

print(max([reading(a),reading(b)]))

#나 뭐한겨
A,B = input().split()

print(max(A[::-1], B[::-1]))

#
print(max([int(i[::-1]) for i in input().split()]))



