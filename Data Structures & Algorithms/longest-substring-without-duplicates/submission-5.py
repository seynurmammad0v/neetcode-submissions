class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}

        i = 0 
        res = 0

        for j in range(len(s)):
            if s[j] in unique:
                i = max(i, unique[s[j]] + 1)
           
            unique[s[j]] = j
            res = max(res,j-i+1)
        return res