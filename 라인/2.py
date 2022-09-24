from typing import List


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    words = chat.split(' ')
    print(words)

    for i in dic:
        i_length = len(i)
        for j in range(0, len(words)):
            length = len(words[j])
            if i == words[j]:
                words[j] = '#' * length
            elif '.' in words[j] and length <= i_length:
                # 점의 갯수를 k에 맞춰서 늘려서 길이를 똑같이하고, .을 뺀 나머지가 같으면 됨
                


    print(words)
    return answer


print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))
print(solution(3, ["abcde", "cdefg", "efgij"], ".. ab. cdefgh .gi. .z."))