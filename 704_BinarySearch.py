'''
Code Link : https://leetcode.com/problems/binary-search/
'''

'''
Problem Statement:

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
'''



class Solution:
def search(self, nums: List[int], target: int) -> int:
    # add two pointers 1) at last position of array 2) at start of array
    high = len(nums)-1
    low = 0


    while(low<=high):
        mid = (high + (high-low)) // 2  # mid
        if nums[mid] == target:
            return mid

        elif(nums[mid] > target):#if number is in lower half change last pointer
            high = mid - 1

        else:
            low = mid + 1# else change location of lower pointer


    return -1
