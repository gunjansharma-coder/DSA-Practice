# Problem: Highest Occurring Element in an Array
# Topic: Hashing
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/plus/dsa/problems/highest-occurring-element

class Solution:
    def mostFrequentElement(self, nums):
        freq={}
        maxx=0
        a=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key, value in freq.items():
            if value>maxx:
                maxx=value
                a=key
            elif value==maxx:
                if a>key:
                    a=key
        return a