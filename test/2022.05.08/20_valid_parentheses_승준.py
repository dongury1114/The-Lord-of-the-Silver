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