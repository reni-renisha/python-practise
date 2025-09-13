class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        max_prof=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_prof=max(max_prof,profit)
            else:
                l=r
            r+=1
        return max_prof        