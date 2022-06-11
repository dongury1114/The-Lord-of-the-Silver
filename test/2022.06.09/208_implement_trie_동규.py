class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p:
                return False
            else:
                p = p[c]
        return '#' in p

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p:
                return False
            else:
                p = p[c]
        return True
