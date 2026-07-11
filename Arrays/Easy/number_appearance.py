# Problem: Find the number in the array that has appeared only once
# Topic: Arrays
# Difficulty: Easy
# Source: LeetCode
# Link: https://leetcode.com/problems/single-number
class Solution:
    def singleNumber(self, nums):
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for i in count:
            if count[i]==1:
                return i