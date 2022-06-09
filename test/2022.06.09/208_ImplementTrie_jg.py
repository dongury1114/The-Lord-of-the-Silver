class Trie:

    def __init__(self):
        self.root = collections.defaultdict()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['*'] = word
        print(cur)
    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        if '*' in cur:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if not p in cur:
                return False
            cur = cur[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
