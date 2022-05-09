class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for st in s:
            if st == ')' or st == ']' or st == '}':
                if not len(stack):
                    return False
                pop = stack.pop()
                if st == ')' and pop != '(':
                    return False
                if st == '}' and pop != '{':
                    return False
                if st == ']' and pop != '[':
                    return False
            else :
                stack.append(st)
        if len(stack):
            return False
        return True
