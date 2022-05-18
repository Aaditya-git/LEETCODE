'''
Code Link: https://leetcode.com/problems/squares-of-a-sorted-array/
'''
'''
Problem Statement:

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # (arr*arr) will not work, it will throw an error
        # so to do square we have multiplied each number with itself using
        # following code and stored the squares in same array.
        nums = [x*x for x in nums]

        # used inbuild sort function and simply returned array.
        nums.sort()
        return nums
