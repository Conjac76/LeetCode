class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.lru = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            if key in self.lru:
                self.lru.remove(key)
                self.lru.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.lru.remove(key)
        elif len(self.map) == self.cap:
            lru_key = self.lru.pop(0)
            del self.map[lru_key]

        self.map[key] = value
        self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)