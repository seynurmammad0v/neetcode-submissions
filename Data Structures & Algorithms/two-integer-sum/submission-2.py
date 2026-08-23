class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            found = target - num 
            if found in seen:
                return [seen[found], index] 
            seen[num] = index
            
        return []
