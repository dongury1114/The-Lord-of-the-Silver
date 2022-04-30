
import sys
import re

sys.stdin = open("input.txt")

s = input()

new_s = re.sub('[^0-9a-zA-Z]', '', s)
new_s= ''.join(new_s)
new_s = new_s.lower()

rev_s = new_s[::-1]
rev_s=''.join(rev_s)

if new_s == rev_s:
    return True
else:
    return False

#isanum: 문자열이 영어, 한글, 숫자로 되어 있으면 참 리턴, 아니면 거짓 리턴
#isalhpa: 문자열이 영어 혹은 한글로 되어 있으면, 참 아니면 거짓

'''두 번째 시도: 테스트 케이스 457번째 숫자가 들어간 경우에서 걸림
import sys

sys.stdin = open("input.txt")

s = list(input())

s = filter(str.isalpha, s)
s= ''.join(s)
s = s.lower()

rev_s = s[::-1]
rev_s=''.join(rev_s)

if s == rev_s:
    print("true")
else:
    print("false")
'''


'''첫시도 실패
import sys

sys.stdin = open("input.txt")


word = list(input())

New_word = ''.join(char for char in word if char.isalnum())

new_word=New_word.lower()

rev_new_word = reversed(new_word)

if new_word == rev_new_word:
    print("True")
else:
    print("False")'
'''