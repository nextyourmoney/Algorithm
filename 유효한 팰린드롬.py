#주어진 문자열리 팰린드롬인지 확인하라, 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
#팰린드롬이라 단어나 문장을 뒤집어도 같은 말이 되는 것.
#입력값: "A man, a plan, a canal: Panama"

#2022.01.14
#분류: 문자열 조작 #파이썬 알고리즘 인터뷰 133p
#난이도 1

# JBC 작성코드 == 쓰래기 코드
import collections
import re


def mine():
    strs = []
    s = input()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    a = len(strs)
    b = 0
    count = 0
    while len(strs) > count:
        if strs[a-1] != strs[b]:
            print("불일치!")
            return False

        else:
            print("일치!")

        a -= 1
        b += 1
        count+=1
    return True

#책 #...천잰가? #리스트
def isPalindrome(self, s:str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():  # isaalnum은 영문자, 숫자 여부 판별 함수이다.
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

#책 #데크 자료형
def isPalindrome(self, s:str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():  # isaalnum은 영문자, 숫자 여부 판별 함수이다.
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop(): #리스트의 pop보다 데큐의 popleft가 속도가 빠르다. O(n)와 O(1)인데 반복되면 O(n^2)와 O(n)으로 된다.
            return False

    return True

#책 #슬라이싱
def isPalindrome(self, s:str) -> bool:
    s = s.lower()

    s= re.sub('[^a-z0-9]','',s)

    return s == s[::-1] #슬라이싱






