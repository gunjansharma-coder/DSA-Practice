# Problem: Check if Array is Sorted
# Topic: Arrays
# Difficulty: Easy
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/data-structure/check-if-an-array-is-sorted/

class Solution:
    def isSorted(self, nums):
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] > nums[i+1]:
                return False
        return True