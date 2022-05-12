# ( 값이 입력되면, (값과 )값을 리스트에 저장
# )게 나오면 
#(리스트에 값이 있는지 확인하고 있으면 빼주고 )이값도 빼줌
#만약 남은 리스트에 )가있거나 (있으면 false
#append. pop

class Solution(object):
    def isValid(self, s):

        stack = []
        table = {
            ')' :'(',
            '}' : '{',
            ']': '[',
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char]!= stack.pop():
                return False
        return len(stack)==0