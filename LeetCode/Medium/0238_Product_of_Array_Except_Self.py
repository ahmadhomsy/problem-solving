"""
Problem: Product of Array Except Self
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1) excluding output

Technique:
- Prefix Product
- Suffix Product

Idea:
Store the product of all elements to the left of each index.
Then traverse from right to left and multiply by the product
of all elements to the right.
This avoids division and achieves O(n) time complexity.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1 
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer