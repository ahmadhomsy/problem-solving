"""
Problem: Valid Anagram
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Frequency Array
- Counting

Idea:
Count the frequency of each character in both strings.
Increment counts for characters in the first string and
decrement counts for characters in the second string.
If all counts are zero at the end, the strings are anagrams.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True