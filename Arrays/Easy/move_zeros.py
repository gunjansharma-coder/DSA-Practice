# Problem: Move all the zeros to the end of the array
# Topic: Arrays
# Difficulty: Easy
# Source:LeetCode
# Link: https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums) -> None:
        j=0
        for i in range(0,(len(nums))):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1

        while j< len(nums):
            nums[j]=0
            j+=1