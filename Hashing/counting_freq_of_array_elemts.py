# Problem: Count Frequency of Each Element in an array
# Topic: Hashing
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/plus/dsa/problems/counting-frequencies-of-array-elements

class Solution:
    def countFrequencies(self, nums):
        freq={}
        a=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for i in freq.items():
            a.append(list(i))
        return a