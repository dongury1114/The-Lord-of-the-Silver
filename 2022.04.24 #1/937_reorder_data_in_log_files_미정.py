import sys
sys.stdin = open("input.txt")
#1)알파벳순으로 2) identifier에 따라 3) 숫자는 순서 유지 
# isdigit, lambda x, sort()

class Solution(object):
    def reorderLogFiles(self, logs):
        letters = []
        digit = []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letters.append(log)

        letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))
        return letters+digit

