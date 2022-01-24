#https://www.acmicpc.net/problem/2941

#문자열들을 리스트에 따로 띄우고 '=' or '-'가 입력되면 카운트 리스트를 중단하고 카운트. 리설트 변수에 추가한다?
import sys
from typing import List

String:str = sys.stdin.readline()
count  = 0

count_List = [i for i in String if i != "="]
