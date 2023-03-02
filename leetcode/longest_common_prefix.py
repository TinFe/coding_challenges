""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
Accepted
2.2M
Submissions
5.4M
Acceptance Rate
40.8% 
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        longest_common_prefix_len = 201
        longest_common_prefix = ''
        # create function to compare two strings and return 
        def compare(str1, str2):
            common_prefix = ''
            str1_len = len(str1)
            str2_len = len(str2)

            if str1_len > str2_len:
                big_str = str1
                small_str = str2
            elif str2_len > str1_len:
                small_str = str1
                big_str = str2
            elif str1_len == str2_len:
                big_str = str1
                small_str = str2

            big_str_len = len(big_str)
            small_str_len = len(small_str)

            index = 0
            
            while index < small_str_len and (big_str[index] == small_str[index]):
                common_prefix += small_str[index]
                index += 1
            return common_prefix

        for i in range(len(strs) - 1):
            comparison = compare(strs[i],strs[i+1])
            print(comparison)
            if len(comparison) < 1:
                return ''
            if len(comparison) < longest_common_prefix_len:
                longest_common_prefix = comparison
                longest_common_prefix_len = len(comparison)
        return longest_common_prefix
