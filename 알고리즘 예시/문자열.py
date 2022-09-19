## replace 함수. replace(a,b)일떄 a를 b로 바꿔줌

def solution(s):
    answer = 0
    a = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
    for i in a:
        s = s.replace(i, str(a.index(i)))
    return int(s)


print(solution("one4seveneight"))