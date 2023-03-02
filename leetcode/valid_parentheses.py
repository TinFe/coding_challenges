"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
3.1M
Submissions
7.7M
Acceptance Rate
40.3%
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    

        stack = []

        if len(s) % 2 != 0:
            return False

        if len(s) == 0:
            return True

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)

            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False

            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False            

            elif i == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


