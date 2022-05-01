#sol.1 내 풀이(lambda 구현은 참조)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
   
        for log in logs:
            if log.split()[1].isdigit(): #숫자가 포함된 log는 [1]부터 있음 // 어려웠음
                digits.append(log)
            else:
                letters.append(log) #그외(문자로만 구성된(식별자 제외) 로그는 letter 리스트에 추가)
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0])) #말도안됨
        return letters+digits

#문자로 구성된 로그가 우선
    #같은 로그이면 식별자 우선순위 [lamda식 사용하자]

#sol.2
def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters=[]
        digits=[]
        for log in logs:
            if log[-1].isdigit(): #숫자가 포함된 로그는 logs[-1]도 숫자기 때문에 굳이 복잡하게 split을 하지 않아도 됐음
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda letter: (letter.split()[1:],letter.split()[0])) #1 다중키 개념 1)알파벳순, 2) 식별자순
        return letters+digits


#람다 -> 식별자가 없는 함수
#람다 충분히 연습하기
#https://ubermensch-with.tistory.com/644