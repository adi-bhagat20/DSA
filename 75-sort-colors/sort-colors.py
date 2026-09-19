class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        m = 0
        h = n - 1
        while m <= h:
            if nums[m] == 0:
                nums[m] , nums[l] = nums[l] , nums[m]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m] , nums[h] = nums[h] , nums[m]
                h -= 1
            
        return 
            
        