#손코딩 까지는 완료했는데, 잘 구현되지 않아, 소스코드 참고
#https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
# 아이디어는 같았는데, 구현이 깔끔한 풀이
def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # 홀수
        tmp = self.check(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # 짝수
        tmp = self.check(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

#중앙에서 퍼져나가게 인덱스 조정해주는 함수
def check(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]









# #투포인터
# s = list(s)
# if len(s) == 1 or s == s[::-1]:
#     print(s)

# while True:
