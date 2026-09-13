class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            s.add(num)
        
        if len(s) != len(nums):
            return True
        
        return False
        