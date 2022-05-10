import collections
s = "cbacdcbc"

# for i in range(len(s)) :
#     m = min(s[i:])
#     if s[i] not in s[i+1:] or s[i] == min:
#         stact.append(s[i])
    
# print(stact)

# print(min(s))

counter = collections.Counter(s)
seen = set()
stack = []

for char in s :
    counter[char] -= 1
    if char in seen :
        continue
    while stack and stack[-1]>char and counter[stack[-1]] >= 1:
        seen.remove(stack.pop())
    seen.add(char) #set은 add
    stack.append(char)

print(''.join(stack))