# 소스: https://deep-flame.tistory.com/m/15
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1: return s

        start, length = 0, 0
        for end in range(len(s)):
            # 기존 substring에서 자신만 추가하여 조건 성립 Ex. aaa
            if s[end-length:end+1] == s[end-length:end+1][::-1]:
                start, length = end-length, length+1
            # 기존 substring에서 자신과 앞을 추가하여 조건 성립 Ex. baaab
            elif end-length-1 >= 0 and s[end-length-1:end+1] == s[end-length-1:end+1][::-1]:
                start, length = end-length-1, length+2

        return s[start:start+length]



#틀린 이
# back = s[::-1]
# ans = []

# if len(s) <=2 and s[0]!=s[1] :
#     print( s[0])
# if len(s) <=2 and s[0] == s[1]:
#     print(s[0]+s[1])
# else:
#     for i in range(len(s)):
#         if back[i] == s[i]:
#             ans.append(back[i])
#         if len(s)<= 2:
#             ans.append(s[i])
#     ans = ''.join(ans)
#     print( ans )