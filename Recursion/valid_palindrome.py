# Problem: Check if the string is palindrome or not
# Topic: Recursion
# Source: Striver A2Z DSA Sheet
# LeetCode: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        def helper(left, right):
            if left >= right:
                return True

            if cleaned[left] != cleaned[right]:
                return False

            return helper(left + 1, right - 1)

        return helper(0, len(cleaned) - 1)