# Problem: Bubble Sort
# Topic: Sorting
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/data-structure/bubble-sort-algorithm/

class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(0,n-1):
            for j in range(0,n-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums