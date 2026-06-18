"""
Problem: Merge Sorted Array
Difficulty: Easy

Time Complexity: O(m + n)
Space Complexity: O(1)

Technique:
- Two Pointers

Idea:
Start from the end of both arrays and place the larger
element at the end of nums1.
This avoids shifting elements and allows merging in-place.
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1