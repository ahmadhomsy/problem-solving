"""
Problem: Container With Most Water
Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
- Greedy

Idea:
Start with pointers at both ends of the array.
Calculate the area formed by the two lines.
Move the pointer with the smaller height inward,
since the area is limited by the shorter line.
Keep track of the maximum area found.
"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0 
        while left < right  :
            w = right - left
            h = min(height[left],height[right])
            max_area = max(max_area , h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
