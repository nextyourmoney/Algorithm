#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라, 대소문자 구분을 하지 않으며, 구두점또한 무시한다.
import collections
import re


def mostwords(paragraph:str, ban:str) -> None:
    words = [word for word in re.sub(r'[^\w]',' ', paragraph) #리스트 컴프리핸션
        .lower().split()
            if word not in ban]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0] #크기 순으로 정렬 #(1)개만큼 리턴

def mostwords2(paragraph:str, ban:str) -> None:
    words = [word for word in re.sub(r'[^\w]',' ', paragraph) #리스트 컴프리핸션
        .lower().split()
            if word not in ban]

    counts = collections.defaultdict(int)#int를 디폴트 값으로 둔다.
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)#파이썬은 argmax를 지원하지 않으므로 key를 지정해주고 해당 값(value)으로 크기 비교 #get은 값 가져오는거 알제?


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
ban = "hit"

mostwords(paragraph, ban)
mostwords2(paragraph, ban)