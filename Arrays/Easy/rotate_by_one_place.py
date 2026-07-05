# Problem: Rotate the array by one place
# Topic: Arrays
# Difficulty: Easy
# Source: Striver's A2Z DSA sheet

class Solution:
    def rotateArray(self, nums):
        if len(nums) <= 1:
            return
        first = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[-1] = first