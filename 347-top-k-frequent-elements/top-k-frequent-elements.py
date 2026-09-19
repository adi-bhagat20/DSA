class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num , 0) + 1

        top_k_ele = sorted(d , key = d.get , reverse = True)[:k]
        return top_k_ele