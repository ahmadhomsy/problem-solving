"""
Problem: Two Sum
Difficulty: Easy

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
Hash Map
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i