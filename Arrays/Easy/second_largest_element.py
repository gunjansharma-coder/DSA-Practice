# Problem: Find the seocnd largest element in an array
# Topic: Arrays
# Difficulty: Easy
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/plus/dsa/problems/second-largest-element?source=strivers-a2z-dsa-track

class Solution:
    def secondLargestElement(self,nums):
        n=len(nums)
        largest=nums[0]
        second=-1
        for i in range(1,n):
            if nums[i]>largest:
                second=largest
                largest=nums[i]
            elif nums[i]>second and nums[i]<largest:
                second=nums[i]
        return second