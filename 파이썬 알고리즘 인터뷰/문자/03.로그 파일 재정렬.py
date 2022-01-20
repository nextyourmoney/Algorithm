#로그를 재정렬 하라. 기준은 다음과 같다.
"""
1.로그의 가장 앞 부분은 식별자다.
2.문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3.식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자로그는 입력 순서대로 한다.

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

from typing import List

def re_log(logs:List[str]) -> None:
     letters, digits = [], []
     for log in logs:
         if log.split()[1].isdigit(): #숫자 구분
             digits.append(log) #숫자는 입력 된 순서대로 출력 딤
         else:
             letters.append(log)
     letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) #람다식을 이용한 문자 정렬, '1A'와 같은 형태에서 A로 정렬을 할 필요가 있기에 순서를 바꾼 후 정렬
     return letters + digits

input = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
re_log(input)