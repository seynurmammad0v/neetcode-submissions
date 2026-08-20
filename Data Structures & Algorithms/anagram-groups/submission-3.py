class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedAnagramsMap =  defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] +=1

            sortedAnagramsMap[tuple(count)].append(s)

        return list(sortedAnagramsMap.values())
