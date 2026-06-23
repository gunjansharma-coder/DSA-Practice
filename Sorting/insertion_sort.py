# Problem: Insertion Sort
# Topic: Sorting
# Source: Striver A2Z DSA Sheet
# Link: https://takeuforward.org/data-structure/insertion-sort-algorithm/

class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            check = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > check:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = check
        return nums