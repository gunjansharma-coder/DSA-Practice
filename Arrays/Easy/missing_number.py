# Problem: Find the missing numbers in an array
# Topic: Arrays
# Difficulty: Easy
# Source: Striver's A2Z DSA sheet

class Solution:
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
