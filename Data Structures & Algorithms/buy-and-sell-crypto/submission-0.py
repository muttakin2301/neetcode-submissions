class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentProfit = 0
        buyDay = 0

        for sellDay in range(1, len(prices)):
            currentProfit = prices[sellDay] - prices[buyDay]

            while currentProfit < 0 and buyDay < sellDay:
                buyDay += 1
                currentProfit = prices[sellDay] - prices[buyDay]

            maxProfit = max(maxProfit, currentProfit)
            # print(maxProfit, buyDay, sellDay)

        return maxProfit