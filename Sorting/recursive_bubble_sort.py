# Problem: Recursive Bubble Sort
# Topic: Sorting - Recursion
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/data-structure/recursive-bubble-sort-algorithm/

class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        def helper(i, j):
            if i == n - 1:
                return nums

            if j == n - i - 1:
                return helper(i + 1, 0)
            
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            return helper(i, j + 1)
        return helper(0, 0)