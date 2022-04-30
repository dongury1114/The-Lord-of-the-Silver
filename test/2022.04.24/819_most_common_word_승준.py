import re

paragraph = 'a, a, a, a, b,b,b,c, c'
banned = ['a']
# banned도 소문자 처리가 필요할 듯

data = dict()

paragraph = re.sub('[^a-zA-Z0-9]', ' ', paragraph).strip()

a = paragraph.lower().split()
b = list()
for i in a:
    
    if (i != ''):
        b.append(i)
        
for i in b:
    if i not in banned:
        data[i] = 0
        
for i in b:
    if i not in banned:
        data[i] += 1
        
print(data)

max_key = max(data, key = data.get)
print(max_key)