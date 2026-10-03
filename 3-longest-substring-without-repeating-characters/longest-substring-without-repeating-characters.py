class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [-1] * 256
        maxLength = 0
        i = j = 0

        while j != len(s):
            # CONCEPT FIX: A character is only a duplicate if it's INSIDE our current window (>= i)
            if seen[ord(s[j])] >= i:
                # Move the left pointer past the old occurrence
                i = seen[ord(s[j])] + 1
            
            # These two steps now run every single turn, cleanly advancing j
            seen[ord(s[j])] = j
            maxLength = max(maxLength, (j - i + 1))
            j += 1
            
        return maxLength
