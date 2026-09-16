class Solution:
    def merge(self , left , right):
        sorted_arr = []
        i , j = 0 , 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])

        return sorted_arr

    def mergeSort(self , nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left_half = self.mergeSort(nums[:mid])
        right_half = self.mergeSort(nums[mid:])

        return self.merge(left_half , right_half)

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.mergeSort(nums)