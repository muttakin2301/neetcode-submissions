class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyDay = 0

        for sellDay in range(1, len(prices)):
            while prices[buyDay] > prices[sellDay]:
                buyDay += 1

            maxProfit = max(maxProfit, (prices[sellDay] - prices[buyDay]))

        return maxProfit