# Problem: Reverse an array and print it using recursion
# Topic: Recursion
# Source: Striver A2Z DSA Sheet

class Solution:

    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n - 1
    
        def helper(left, right):
            if left >= right:
                return
            arr[left], arr[right] = arr[right], arr[left]
            helper(left + 1, right - 1)
    
        helper(left, right)