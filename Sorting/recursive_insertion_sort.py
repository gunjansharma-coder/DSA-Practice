# Problem: Recursive Insertion Sort
# Topic: Sorting - Recursion
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/data-structure/recursive-insertion-sort-algorithm/

class Solution:
    def insertionSort(self, nums):
        n=len(nums)
        def helper(i,j,check):
            if i==n:
                return nums
            if (j>=0 and nums[j]>check):
                nums[j+1]=nums[j]
                return helper(i,j-1,check)
            nums[j+1]=check
            if i+1 == n:
                 return nums
            return helper(i+1, i, nums[i+1])
        return helper(1,0,nums[1])