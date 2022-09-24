def solution(s):
    new_s = s.rstrip()
    words = new_s.split(" ")

    return len(words[-1])


print(solution("Hello World"))
print(solution("   fly me   to   the moon  "))
print(solution("luffy is still joyboy"))