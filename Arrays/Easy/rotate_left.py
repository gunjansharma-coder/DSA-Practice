class Solution:
    def rotate(self, nums, k: int) -> None:
        n=len(nums)
        for i in range(0,n):
            if k>0:
                temp=nums[i]
                nums[i]=nums[-k]
                nums[-k]=temp
                k-=1
        return nums
obj=Solution()
z=obj.rotate([1,2,3,4,5,6,7],3)
print(z)
