'''
Code Link: https://leetcode.com/problems/search-insert-position/
'''

'''
Problem Statement:

Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
#the Logic of binary search.
        while(low<=high):
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return high+1 #if number not found then it will return the index
                      #where the number belonged in array.
