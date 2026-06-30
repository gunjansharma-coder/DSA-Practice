# Problem: Find the largest element in an array
# Topic: Arrays
# Difficulty: Easy
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/arrays/largest-element-in-an-array/

class Solution:
    def largestElement(self, nums):
        n=len(nums)
        maxx=nums[0]
        for i in range(0,n):
            if nums[i]>maxx:
                maxx=nums[i]
        return maxx