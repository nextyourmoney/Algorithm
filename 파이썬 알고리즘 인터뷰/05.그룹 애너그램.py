"""
문자열 배열을 받아 애너그램 단위로 그룹핑하시오
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from typing import List
import collections

def anagrams (group:List[str]) -> None:
   anagrams = collections.defaultdict(list)

   for word in group:
       anagrams[''.join(sorted(word))].append(word)

   return list(anagrams.values())

anagrams(["eat","tea","tan","ate","nat","bat"])
