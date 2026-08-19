class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        simbols = {}
        if len(s)!= len(t):
            return False

        for c in s:
            if c in simbols:
                simbols[c] = simbols[c]+1
            else:
                simbols[c] = 1

        for c in t:
            if c not in simbols: 
                return False
            else:
                if simbols[c] == 0:
                    return False
                else: 
                    simbols[c] = simbols[c]-1

        return True
        