class Solution(object):
    def maxProfit(self, prices):
        minprice=prices[0]
        maxprice=prices[0]
        maxprofit=0
        for price in prices :
            if price < minprice:
                minprice=price
                maxprice=price
            if price > maxprice:
                maxprice=price

            maxprofit=max(maxprofit,maxprice-minprice)

        return maxprofit