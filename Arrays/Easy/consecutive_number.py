# Problem: Find the Maximum Consecutive Ones in an Array
# Topic: Arrays
# Difficulty: Easy
# Source: LeetCode
# Link: https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        temp =0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if count>temp:
                    temp=count
                count=0
        return max(temp,count)
        