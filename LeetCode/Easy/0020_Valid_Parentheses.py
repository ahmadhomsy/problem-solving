"""
Problem: Valid Parentheses
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Stack
- Hash Map

Idea:
Use a stack to store opening brackets.
When a closing bracket is encountered,
check if it matches the most recent opening bracket.
The string is valid if all brackets are matched
and the stack is empty at the end.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in mapping:
                if not stack or stack.pop() != mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack
