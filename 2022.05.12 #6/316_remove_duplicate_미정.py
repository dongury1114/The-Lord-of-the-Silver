import collections
s = "cbacdcbc"

def removeDuplicateLetters(s):
    counter = collections.Counter(s)
    print(counter)
    seen = set()
    stack = []
    for char in s: # dictionary 각각 원소 다 없어질때까지
        counter[char] -= 1
        if char in seen:
            continue
        #char index가 stack[-1]인덱스보다 작은 경우 
        while stack and char < stack[-1] and counter[stack[-1]]>0:
            print(stack,seen,counter)
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        print(stack, seen)
    return ''.join(stack)

print(removeDuplicateLetters(s))

##재귀

# def removeDuplicateLetters(self, s:str) -> str:
# set을 통해 s 중복을 없앤다. char 값의 index부터를 suffix라고 정의하고
#     for char in sorted(set(s)):
#         suffix = s[s.index(char):]
        #일치할 때 분리 진행 
#         if set(s) == set(suffix):
#             return char + self.removeDuplicateLetters(suffix.replace(char,''))
#     return ''
