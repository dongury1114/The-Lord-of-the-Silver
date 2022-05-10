class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        counter, setlist = collections.Counter(s), set()
        stack = []
        for i in s:
            counter[i] -= 1
            if i in setlist:
                continue
            while stack and stack[-1] > i and counter[stack[-1]] > 0:
                setlist.remove(stack.pop())
            stack.append(i)
            setlist.add(i)
            
        return (''.join(stack))
