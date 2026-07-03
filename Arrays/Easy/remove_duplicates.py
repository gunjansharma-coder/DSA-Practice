# Problem: Remove Duplicates from Sorted Array
# Topic: Arrays
# Difficulty: Easy
# Source: LeetCode
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k