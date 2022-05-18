'''
Code Link: https://leetcode.com/problems/rotate-array/
'''

'''
Problem Statement :

Given an array, rotate the array to the right by k steps,
where k is non-negative.
'''
# method 1:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # here we have used positive indexing
        # for last element pointer
        l=len(nums)

        # for index where we have to slice
        k=k%l

        # condition for empty array
        if k==0:
            pass
        else:
            # store all the numbers from 0th postion to the givem index in temp.
            temp=nums[0:l-k]

            # remaining elements to first k index
            nums[0:k]=nums[l-k:l]

            # and store numbers from kth index to last element from temp.
            nums[k:l]=temp

        return nums

# else simple code using negative indexing.
# method 2:

print(arr[-index:]+arr[:-index])
