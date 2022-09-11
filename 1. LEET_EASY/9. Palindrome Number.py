'''
 Integer x에 대해 만약 x가 팰린드롬수라면 true를 리턴하기
 거꾸로 읽어도 똑같은 것
'''

def isPalindrome(x):
    if x < 0:
        return False

    new_x = str(x)

    if new_x == new_x[::-1]:
        return True
    else:
        return False

'''
    1. 음수일때는 앞에 -가 붙어 거꾸로 읽으면 회문이 되지 못함
    2. 문자열로 바꾼뒤 앞뒤로 똑같은지만 확인인
'''