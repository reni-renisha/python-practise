class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for i in prices[1:]:
            min_price=min(i,min_price)
            profit=i-min_price
            max_profit=max(profit,max_profit)
        return max_profit