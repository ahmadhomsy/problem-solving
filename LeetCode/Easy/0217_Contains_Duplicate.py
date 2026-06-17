"""
Problem: Contains Duplicate
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Hash Set

Idea:
Store each number in a set.
If a number already exists in the set,
a duplicate has been found.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: 
                return True
            seen.add(num)   
        return False