#문자열을 뒤집는 함수 정의, 입력값은 문자 배열이며, 리턴 없이 리스트 내부 직접 제어

from typing import List

def levers(s:List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)

def reverseString(s:List[str]) -> None:
    s.reverse()
    print(s)

def reverseSlice(s:str) -> None:
    s = s[::-1]
    print(s)

s = ["h","e","l","l","o"]
levers(s)
reverseString(s)
reverseSlice("hello")