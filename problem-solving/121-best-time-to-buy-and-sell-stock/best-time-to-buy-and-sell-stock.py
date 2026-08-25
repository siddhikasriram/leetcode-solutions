class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

    
        buy = prices[0]
        i = 1
        profit = 0

        while i < len(prices):
            if prices[i] < buy:
                buy = prices[i]
                print(buy)
            else: 
                profit = max(profit, prices[i] - buy)
                print (profit)
            i += 1
        return profit


        

        
      


    