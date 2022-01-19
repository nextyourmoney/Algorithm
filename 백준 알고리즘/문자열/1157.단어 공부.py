#https://www.acmicpc.net/problem/1157
import collections

def word_count_mine (word:str) -> str:
    word_count_dic = collections.defaultdict(int)

    for i in list(word):
        word_count_dic[i] += 1

    max_key = [key for key, value in word_count_dic.items() if max(word_count_dic.values()) == value]
    if len(max_key) > 1:
        print("?")
    else:
        print(max_key[0])

def word_count_other (word:str) -> str:
    unique_words = list(set(word))

    cnt_list = []
    for x in unique_words:
        cnt = word.count(x)
        cnt_list.append(cnt)

    if cnt_list.count(max(cnt_list)) > 1:
        print('?')
    else:
        max_index = cnt_list.index(max(cnt_list))
        print(unique_words[max_index])

word = input().upper()
word_count_mine(word)
word_count_other(word)




