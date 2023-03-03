"""
DESCRIPTION:

Define n!! as

n!! = 1 * 3 * 5 * ... * n if n is odd,

n!! = 2 * 4 * 6 * ... * n if n is even.

Hence 8!! = 2 * 4 * 6 * 8 = 384, there is no zero at the end. 30!! has 3 zeros at the end.

For a positive integer n, please count how many zeros are there at the end of n!!.

Example:

30!! = 2 * 4 * 6 * 8 * 10 * ... * 22 * 24 * 26 * 28 * 30 
30!! = 42849873690624000 (3 zeros at the end)
"""
def count_zeros_n_double_fact(n): 
    # Please try to count something. 
    double_fact = 1
    if n % 2 == 0:
        for i in range(1,n+1):
            if i % 2 == 0:
                double_fact *= i
                
    elif n % 2 != 0:
        for i in range(1,n+1):
            if i % 2 != 0:
                double_fact *= i
        
    double_fact_str = str(double_fact)
    num_of_zeros = 0
    for c in reversed(double_fact_str):
        if c != '0':
            break
        elif c == '0':
            num_of_zeros += 1
            
    return num_of_zeros
