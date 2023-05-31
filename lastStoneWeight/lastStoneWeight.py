class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)
            if stone1 < stone2:
                stone2 = stone2 - stone1
                stone2 *= -1 
                heapq.heappush(stones, stone2)
            elif stone1 > stone2:
                stone1 = stone1 - stone2
                stone1 *= -1 
                heapq.heappush(stones, stone1)
            
        if len(stones) == 0:
            return 0

        return -1 * stones[0]
