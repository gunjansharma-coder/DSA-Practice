# Problem: Remove Duplicates from Sorted Array
# Topic: Arrays
# Difficulty: Easy
# Source: LeetCode

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        # Reverse the whole array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])

