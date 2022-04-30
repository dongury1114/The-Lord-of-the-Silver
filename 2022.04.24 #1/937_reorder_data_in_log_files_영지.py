class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        a = []
        for i in logs :
            if i.split()[1].isalpha() :
                a.append(i)
        a.sort(key=lambda x : (x.split()[1:],x.split()[0]))
        print(a)
        for i in logs :
            if i.split()[1].isalpha() == False :
                a.append(i)
                
        return a