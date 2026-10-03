class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}

        for idx , num in enumerate(nums):
            if (target - num) in d:
                return [idx , d[target - num]]
            
            d[num] = d.get(num , 0) + idx
        