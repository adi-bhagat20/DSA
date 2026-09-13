class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lst1 = sorted(s)
        lst2 = sorted(t)

        for i in range(len(lst1)):
            if lst1[i]!=lst2[i]:
                return False
            
        return True