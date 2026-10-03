class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        countOfZeros = 0
        product = 1
        idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                countOfZeros += 1
                idx = i
                continue
            product = product*nums[i]
        
        if countOfZeros > 1:
            return [0 for _ in range(len(nums))] 
        elif countOfZeros == 1:
            nums = [0 for _ in range(len(nums))]
            nums[idx] = product
        else:
            for i in range(len(nums)):
                nums[i] = product // nums[i]
        
        return nums