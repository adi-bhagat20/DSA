class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = []
        temp = [[] for _ in range(len(nums) + 1)]
        d = {}
        for num in nums:
            d[num] = d.get(num , 0) + 1
        
        for n , c in d.items():
            temp[c].append(n)
        
        for i in range(len(temp) - 1, 0 , -1):
            for num in temp[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans