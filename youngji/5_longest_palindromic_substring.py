
s = "bb"

l = len(s)

# maxi = 0
# for start in range(l) :
#     for end in range(l) :
#         words = s[start:end+1]
#         if words == words[::-1] :
#             if len(words) > maxi :
#                 result = words
#                 maxi = len(words)

# print(''.join(result))

if l <= 1 :
    print(s)

def check(start,end):
    while start >= 0 and end < l :
        word = s[start:end+1]
        if word == word[::-1] :
            start -= 1
            end += 1
        else : break
    return s[start+1:end] #!!!!!!!!!!!!!!!!인덱스 진짜 헷갈린다. +1 -1

result =''
maxi = 0
for i in range(l-1) :
    a = check(i,i+1)
    b = check(i,i+2)
    result = max(result,a,b,key=len)


print(result)