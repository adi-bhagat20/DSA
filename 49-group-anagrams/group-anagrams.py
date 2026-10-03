class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for word in strs:
            lst = [0]*26

            for ch in word:
                lst[ord(ch) - ord('a')] +=1

            key = tuple(lst)

            if key not in d:
                d[key] = []
            d[key].append(word)
        
        return list(d.values())