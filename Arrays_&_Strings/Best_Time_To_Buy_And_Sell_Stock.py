class Solution(object):
    def maxProfit(self, prices):
        profit=0
        tmin= max(prices)
        for i in range(len(prices)):
            if prices[i] < tmin:
                tmin=prices[i]
            if prices[i]-tmin >profit:
                profit= prices[i]-tmin
        
        return profit
