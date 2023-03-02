"""
7. Reverse Integer
Medium
9.9K
11.7K
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
Accepted
2.5M
Submissions
9.1M
Acceptance Rate
27.4%

"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output = ''
        x = str(x)
        last_index = -len(x)
        index = -1
        while index >= last_index:
            output += x[index]
            index -= 1
        if output[-1] == '-':
            output = output[0:len(output)-1]
            output = -1 * int(output)
            
        if int(output) > 2**31 or int(output) < -2**31:
            return 0
        return int(output)
                
