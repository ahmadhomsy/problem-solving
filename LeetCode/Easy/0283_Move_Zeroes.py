"""
Problem: Move Zeroes
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
- In-Place Array Modification

Idea:
Use a pointer to track the position of the next
non-zero element. Whenever a non-zero value is found,
swap it into the correct position and move the pointer forward.
This keeps all non-zero elements in order while moving
zeros to the end.
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0