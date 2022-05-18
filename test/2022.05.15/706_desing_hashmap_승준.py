from collections import defaultdict

class MyHashMap:

    def __init__(self):
        self.data = defaultdict(dict)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if self.data[key] or self.data[key] == 0:
            return self.data[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.data[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)