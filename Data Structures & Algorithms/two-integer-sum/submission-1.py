class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapOfNumbers = {}
        for index,n in enumerate(nums):
            if target-n in mapOfNumbers:
                return [mapOfNumbers[target-n],index]
            mapOfNumbers[n] = index
        return []