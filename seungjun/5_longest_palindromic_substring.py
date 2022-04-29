# 궁금한 점 : 다들 주석은 어디에, 어떻게 작성하나요? 컨벤션 같은 거 아는 게 있는지
import sys

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lt, rt):
            while lt >= 0 and rt <= len(s) - 1 and s[lt] == s[rt]:
                lt -= 1
                rt += 1
                
            return s[lt + 1:rt]
        
        if len(s) < 2 and s == s[::-1]:     # 문자의 길이가 1이면 그 자체로 팰린드롬이므로 바로 반환. 혹은 앞 뒤로 똑같으면 이미 팰린드롬이므로 바로 반환.
            return s
        
        res = ''
        for i in range(len(s) - 1):         # lt -= 1과 rt += 1을 겪은 다음 while문의 조건을 충족시키지 못하고 끝나기 때문에 이를 원복해주는 만큼 반환해줘야 한다.
            res = max(res, expand(i, i + 1), expand(i, i + 2), key = len)
            
        return res