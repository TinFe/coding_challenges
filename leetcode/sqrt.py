"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
"""

def mysqrt(x):
        """
        :type x: int
        :rtype: int
        """
        top = x
        middle = x / 2
        bottom = 0
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x > 1:
            iterations = 0
            while True:
                if round(abs(middle * middle - x),6) < 1:
                    return iterations, int(middle)
                elif middle * middle > x:
                    top = middle
                    middle = (bottom + top) / 2
                elif middle * middle < x:
                    bottom = middle
                    middle = (bottom + top) / 2
                iterations +=1
