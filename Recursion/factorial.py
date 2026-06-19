# Problem: Print the factorial of a number using recursion
# Topic: Recursion
# Source: Striver A2Z DSA Sheet

class Solution:
    def factorial(self, n):
        if n==0:
            return 1
        else:
            return n* (self.factorial(n-1))