class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [-1]*256
        maxLength = 0
        i = j = 0

        while j != len(s):
            if seen[ord(s[j])] >= i:
                i = seen[ord(s[j])] + 1
            
            seen[ord(s[j])] = j
            maxLength = max(maxLength , (j - i + 1))
            j+=1
        return maxLength