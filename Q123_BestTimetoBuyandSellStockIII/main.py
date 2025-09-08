class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        # Initialize states
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        
        for price in prices:
            buy1 = max(buy1, -price)         # First buy (spend money)
            sell1 = max(sell1, buy1 + price) # First sell (gain profit)
            buy2 = max(buy2, sell1 - price)  # Second buy (use profit from sell1)
            sell2 = max(sell2, buy2 + price) # Second sell (final profit)
        
        return sell2
