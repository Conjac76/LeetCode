class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximumProfit = 0

        while right < len(prices):
            if(prices[left] < prices[right]):
                tempProfit = prices[right] - prices[left]
                if(tempProfit > maximumProfit):
                    maximumProfit = tempProfit
            else:
                left = right

            right = right + 1

        return maximumProfit            
            