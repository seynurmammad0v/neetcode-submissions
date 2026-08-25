class Solution:
    # [2,20,4,10,3,4,5]
    # [2,3,4,4,5,10,20]
    # {2,3,4,5,10,20}
    # [2, 3, 4, 5].
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numbers = set(nums)

        maxLen = 0
        for number in numbers:
            currLen = 0
            if (number-1) not in numbers:
                while number in numbers:
                    number+=1
                    currLen+=1
            maxLen = max(maxLen,currLen)

        return maxLen