class Solution:
    def isValid(self, s: str) -> bool:
        p = dict()
        p[')'] = '('
        p['}'] = '{'
        p[']'] = '['

        stack = []

        for i in range(len(s)) :
            if s[i] in p.values() :
                stack.append(s[i])
            else :
                if not stack or p[s[i]] != stack[-1] :
                    return False
                stack.pop()
                
        if stack : return False
        
        return True