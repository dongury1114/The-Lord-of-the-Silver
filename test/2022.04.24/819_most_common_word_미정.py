#금지된 단어를 제외하고 가장 많이 쓰인 단어를 출력 , 대소문자 특수문자 구분 없이 입력, 소문자로 출력해야함.
#띄어쓰기 위주로 나눠서 그걸 dictionary에 담는다
# key 값이 banned 인거 제외하고 value가 높은 걸 출력

import re 

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        new_text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', paragraph).lower()
        text = new_text.split()
        ans = dict()
        for word in text:
            ans[word] = ans.get(word, 0)+1
        for ban in banned:
            del ans[ban]
        max_key = max(ans, key=ans.get)
        return max_key