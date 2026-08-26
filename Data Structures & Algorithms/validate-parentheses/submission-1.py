class Solution:
    def isValid(self, s: str) -> bool:
        seenBrackets = []
        brackets = {'[':']','{':'}','(':')'}
        for c in s:
            if c in brackets: 
                seenBrackets.append(c)
            else:
                if len(seenBrackets) == 0:
                    return False
                if c != brackets[seenBrackets.pop()]:
                    return False
        
        return  len(seenBrackets) == 0
                