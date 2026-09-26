class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')' : '(' , ']' : '[' , '}' : '{'}

        for ch in s:
            if ch in d.values():
                stack.append(ch)
            elif ch in d.keys():
                if not stack or d[ch] != stack.pop():
                    return False
        
        return not stack