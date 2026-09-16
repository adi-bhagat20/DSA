class Solution:
    def merged(self , left , right):
        i , j = 0 , 0
        sorted_arr = []

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
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merged(left_half , right_half)