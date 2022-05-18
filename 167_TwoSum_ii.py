'''
Code Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

'''
Problem Statement:
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= first < second <= numbers.length.
Return the indices of the two numbers, index1 and index2,
as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
You may not use the same element twice.
'''

# Method 1.
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:

    flag1 = 0 # first pointer
    flag2 = len(nums)-1 #second pointer at the end of the array

    for i in range(len(nums)):

        if nums[flag1]+nums[flag2]==target:  #if first plus last number == target return their index
            return [flag1+1,flag2+1]

        # else if first plus last last number> target then move the last pointer to the left.
        elif nums[flag1] + nums[flag2] > target:
            flag2 = flag2 - 1

        # else if first plus last last number< target then move the first pointer to the right.
        elif nums[flag1] + nums[flag2] < target:
            flag1 = flag1 + 1

# Method 2:
'''
Use BruteForce i.e. for loops . do it in O(n^2).
'''
