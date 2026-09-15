class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}

        for word in strs:
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord('a')]+=1

            key = tuple(count)

            d.setdefault(key , []).append(word)

        return list(d.values())