# Problem: Using linear search find the target value's first index
# Topic: Arrays
# Difficulty: Easy
# Source: Striver's A2Z DSA sheet
# Link: https://takeuforward.org/plus/dsa/problems/linear-search

class Solution:
    def linearSearch(self, nums, target):
        index=-1
        for i in range(0,len(nums)):
            if nums[i]==target:
                index=i
                break
        return index
