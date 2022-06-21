# 대소문자를 구별하지 않기에 전부 대문자 변환
s = input().upper()

set_s = set(s)
cnt_list = []

for word in set_s:
    # 글자의 수를 세서 cnt_list 에 추가해놓기
    cnt = s.count(word)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
elif cnt_list.count(max(cnt_list)) == 1:
    new_s = list(set_s)
    print(new_s[cnt_list.index(max(cnt_list))])