s = "pwwkew"

s = list(s)

if not s:
    print(0)

tmp = [s[0]]

for i in range(1, len(s)):
    if s[i] in tmp:
        tmp = []
    else:
        tmp.append(s[i])
print(tmp)
