class Solution:
    def isValid(self, s: str) -> bool:
        seenBrackets = []
        brackets = {'[':']','{':'}','(':')'}
        for c in s:
            if c in brackets: 
                seenBrackets.append(c)
            else:
                if not seenBrackets or c != brackets[seenBrackets.pop()]:
                    return False
        
        return len(seenBrackets) == 0
                