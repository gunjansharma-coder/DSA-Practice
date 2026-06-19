# Problem: Print numbers from 1 to N using recursion
# Topic: Recursion
# Source: Striver A2Z DSA Sheet

class Solution:
    def printNumbers(self, n):
        if n==0:
            return 1
        else:
            self.printNumbers(n-1)
            print(n)