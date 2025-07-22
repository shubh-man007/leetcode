class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - buy
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                buy = price

        return max_profit
