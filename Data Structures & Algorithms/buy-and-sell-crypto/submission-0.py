class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #define a maximum and minimum price
        #Iterate through array 
        #Calcualte price at current sell
        #If price is lower than min, update
        #If current profit is greater than maximum, update

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)

        return maxP

        

        