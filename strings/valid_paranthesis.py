"""
Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for ele in s:
            if ele == "(":
                stack.append(ele)
            else:
                if len(stack) == 0:
                    stack.append(ele)
                
                elif stack[-1] == ele:
                    stack.append(ele)
                
                else:
                    stack.pop(-1)

        return len(stack)