class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        p = []
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - buy
            if profit > 0:
                buy = buy
            else:
                buy = prices[i]
            p.append(profit)

        if len(p) > 0 and max(p) > 0:
            return max(p)
        return 0
