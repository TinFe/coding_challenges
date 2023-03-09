"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # create array storing the number of ways to climb a step such that the index of each item
        # represents n, the total number of stars
        ways_to_climb = [1]
        for i in range(n):
            if i < 1:
                ways_to_climb.append(1)
            else:
                ways_to_climb.append(ways_to_climb[i] + ways_to_climb[i-1])

        return ways_to_climb[-1]
    
        
