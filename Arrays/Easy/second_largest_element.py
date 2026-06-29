# Problem: Find the seocnd largest element in an array
# Topic: Arrays
# Difficulty: Easy
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/arrays/second-largest-element-in-an-array/

class Solution:
    def secondLargest(self,nums):
        n=len(nums)
        largest=nums[0]
        second=-1
        for i in range(1,n):
            if nums[i]>largest:
                second=largest
                largest=nums[i]
            if nums[i]>second and nums[i]<largest:
                second=nums[i]
        return second
    
obj=Solution()
z=obj.secondLargest([2, 5, 5, 3])
print(z)