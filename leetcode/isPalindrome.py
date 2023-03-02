"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
Accepted
3M
Submissions
5.5M
Acceptance Rate
53.4%
"""

class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num < 0:
            return False
        
        num_string = str(num)
        reverse = ''
        
        x = len(num_string)-1
         
        while x>= 0:
            reverse += num_string[x]
            x -= 1
            
        if num_string == reverse:
            return True
        else:
            return False
