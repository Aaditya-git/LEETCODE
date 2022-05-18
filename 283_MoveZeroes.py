'''
Code Link : https://leetcode.com/problems/move-zeroes/
'''

'''
Problem Statement:

Given an integer array nums,
move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
'''

#Method 1) best time complexity

nums = list(map(int,input().split()))
lastFound = 0 #first pointer
for i in range(len(nums)):
    if nums[i] != 0:
        nums[lastFound],nums[i] = nums[i],nums[lastFound]
        lastFound += 1
print(nums)


# Method 2) with two empty arrays
'''

zero = []
nonZero = []
for i in range(0,len(arr)):
    if arr[i] != 0:
        nonZero.append(arr[i])

    else:
        zero.append(arr[i])

print(nonZero + zero)
'''
