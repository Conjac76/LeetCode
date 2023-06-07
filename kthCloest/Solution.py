class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        pairs = []
        result = []
        for i in points:
            x = i[0]
            y = i[1]
            dSquare = y * y + x * x
            d = sqrt(dSquare)
            heapq.heappush(heap, (d, [x, y]))

        smallest = heapq.nsmallest(k, heap)[-1][0]


        while heap and len(result) < k:
            d, point = heapq.heappop(heap)
            if d <= smallest:
                result.append(point)

        return result