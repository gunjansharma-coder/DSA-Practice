# Problem: Print the sum of first N natural numbers using recursion
# Topic: Recursion
# Source: Striver A2Z DSA Sheet

class Solution:
    def NnumbersSum(self, N):
        if N==0:
            return 0
        else:
            return N+ self.NnumbersSum(N-1)    