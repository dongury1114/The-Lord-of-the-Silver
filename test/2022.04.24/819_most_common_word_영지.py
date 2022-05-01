# 1. 쪼개서 문자만 리스트 담기 - 소문자로 통일
# 2. 금지된 단어 제외 
# 3. 리스트 돌면서 새로운 단어 나오면 저장하거 이미 나온 단어 나어면 숫자세기 (딕셔너리?)
# 4. 숫자가 제일 큰 단어 출력

import re
from typing import Counter


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

banned = [ x.lower() for x in banned]
paragraph = re.sub('[^0-9a-zA-Z]',' ',paragraph)
#list(filter(str.isalpha,paragraph.split())) #영어 특수문자 붙어있으면 특수문자만 사라지는게 아니라 해당 문자열이 통쨰로 사라짐
paragraph = [ x.lower() for x in paragraph.split()]
print(paragraph)

# for i in banned :
#       if i in paragraph :
#           paragraph.remove(i) #하나만 삭제됨
paragraph = [i for i in paragraph if i not in banned]

cnt = Counter(paragraph) # 딕셔너리 형태
# print(cnt)
print(cnt.most_common(1)[0][0])

