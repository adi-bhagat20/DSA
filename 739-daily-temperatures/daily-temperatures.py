class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        stack = [] #pair : [temp , idx]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp , stackIdx = stack.pop()
                ans[stackIdx] = i - stackIdx
            stack.append([t , i])
        return ans