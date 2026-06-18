"""
Problem: Group Anagrams
Difficulty: Medium

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)

Technique:
- Hash Map
- Sorting
- Grouping

Idea:
Sort each string to create a unique key.
Words that are anagrams will have the same sorted form.
Use a hash map to group all words sharing the same key.
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(word)
        return list(groups.values())