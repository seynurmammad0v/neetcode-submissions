class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        fast, slow = 1,0

        while fast < len(prices):
            if prices[slow]>prices[fast]:
                slow = fast
            else:
                profit = max(prices[fast]-prices[slow],profit)
            
            fast+=1
        
        return profit