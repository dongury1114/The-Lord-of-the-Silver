class MyHashMap:

    def __init__(self):
        self.dic = dict()

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        return self.dic[key]

    def remove(self, key: int) -> None:
        if key not in self.dic.keys() :
            return
        del self.dic[key]
 