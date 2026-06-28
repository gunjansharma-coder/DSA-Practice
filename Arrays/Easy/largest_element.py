class Solution:
    def largestElement(self, nums):
        n=len(nums)
        maxx=0
        for i in range(0,n):
            if nums[i]>maxx:
                maxx=nums[i]
        return maxx