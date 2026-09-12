class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        counter = {}
        l = 0
        max_freq=0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1            

            max_freq = max(counter[s[r]],max_freq)
            replacements = r - l +1 - max_freq 
            
            if replacements <= k:
                res = max(r-l+1,res)
            else: 
                counter[s[l]] -=1
                l+=1
        
        return res