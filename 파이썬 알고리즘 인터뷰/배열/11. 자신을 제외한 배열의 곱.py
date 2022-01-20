from typing import List
def mycal (nums:List) -> List:
    out = []
    p = 1

    #왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p*nums[i]

    #왼쪽 곲 결과에 오른쪽 값을 차례대로 곱한다.
    p = 1
    for i in range(len(nums) - 1, - 1, -1):
        out[i] = out[i] * p
        p = p*nums[i]

    print(out)
    return out

a = [1,2,3,4]

mycal(a)
