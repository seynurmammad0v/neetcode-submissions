class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsSubLst = defaultdict(list)

        count = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] +=1
            anagramsSubLst[tuple(count)].append(s)
        return list(anagramsSubLst.values())