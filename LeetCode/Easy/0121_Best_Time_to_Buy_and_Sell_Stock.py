"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Greedy
- One Pass

Idea:
Track the minimum stock price seen so far.
For each price, calculate the potential profit if sold today.
Update the maximum profit whenever a better profit is found.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0            
        for price in prices[1:]: 
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit