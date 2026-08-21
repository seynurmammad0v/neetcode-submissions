class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, value in count.items():
            freq[value].append(key)

        res = []

        for item in reversed(freq):
            if len(res)>= k:
                break   
            
            for i in item:
                res.append(i)
    

        return res