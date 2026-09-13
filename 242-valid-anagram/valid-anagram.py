class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lst = list(s)

        for ch in t:
            if ch in lst:
                lst.remove(ch)

        if len(lst) != 0:
            return False
        
        return True