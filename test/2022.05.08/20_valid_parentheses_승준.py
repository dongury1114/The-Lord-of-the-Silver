class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            
            else:
                if not stack:
                    return False
                
                if (x == ')' and stack[-1] == '(') or (x == '}' and stack[-1] == '{') or (x == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        else:
            return True
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        s_dict = {')': '(', '}': '{', ']': '['}
        
        for x in s:
            if x in s_dict.values():
                stack.append(x)
            else:
                if stack and s_dict[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        else:
            return True