# Runtime: 1012 ms, faster than 62.35% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 52.72% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        current_min_day = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            min_price = prices[current_min_day]
            if current_price < min_price:
                current_min_day = i
            if max_p < current_price - min_price:
                max_p = current_price - min_price

        return max_p