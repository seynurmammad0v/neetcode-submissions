class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedAnagramsMap = {}
        for str in strs: 
            sortedStr = "".join(sorted(str)) 
            sortedAnagramsMap.setdefault(sortedStr,[]).append(str)
        
        return list(sortedAnagramsMap.values())