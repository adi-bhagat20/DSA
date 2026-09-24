class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        maxSeq = 0
        
        # Iterate over the SET to avoid redundant checks on duplicate numbers
        for num in s:
            if (num - 1) not in s:
                # it is a start sequence
                temp = num
                curSeq = 1
                while (temp + 1) in s:
                    temp += 1
                    curSeq += 1
                maxSeq = max(maxSeq, curSeq)
            
        return maxSeq
