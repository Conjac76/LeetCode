class TimeMap:
    def __init__(self):
        self.myMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []
        self.myMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.myMap:
            data = self.myMap[key]
            left = 0
            right = len(data) - 1
            result = ""
            while left <= right:
                mid = (left + right) // 2
                if data[mid][0] <= timestamp:
                    result = data[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        return ""