class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        maxsell = 0
        p = []
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - buy
            if profit > 0:
                maxsell = profit
                buy = buy
            else:
                buy = prices[i]
            p.append(profit)

        if len(p) > 0:
            x = max(p)
            if x > 0:
                return x
            else:
                return 0
        else:
            return 0
