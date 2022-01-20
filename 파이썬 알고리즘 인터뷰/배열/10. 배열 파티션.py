#n개의 페어를 이요한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

from typing import List
#1
def arrayPairsum(nums:List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for i in nums:
        pair.append(i)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

#권장되는 파이썬 형식의 해법

def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
