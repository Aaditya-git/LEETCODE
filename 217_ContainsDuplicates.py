'''
Code Link: https://leetcode.com/problems/contains-duplicate/
'''

'''
Problem Statement:
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''
# StraightForward Solution.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len1 = len(nums)
        arr =  list(set(nums))
        len2 = len(arr)

        if len1>len2:
            return True
