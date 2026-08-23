class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        sortedTopK = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            sortedTopK[cnt].append(num)

        result = []

        for i in range(len(sortedTopK)- 1, -1, -1):
            if len(result) == k:
                return result
            for item in sortedTopK[i]:
                result.append(item)

        return result

