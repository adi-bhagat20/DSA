class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)
        product = 1
        idx = -1
        countOf0s = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                idx = i
                countOf0s += 1
                if countOf0s > 1:
                    return ans
                continue
            product *= nums[i]
        
        if countOf0s == 1:
            ans[idx] = product
            return ans
        
        for i in range(len(nums)):
            ans[i] = product // nums[i]

        return ans