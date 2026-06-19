# Problem: Print numbers from N to 1 using recursion
# Topic: Recursion
# Source: Striver A2Z DSA Sheet

class Solution:
    def printNumbers(self, n):
        if n==0:
            return
        else:
            print(n)
            self.printNumbers(n-1)