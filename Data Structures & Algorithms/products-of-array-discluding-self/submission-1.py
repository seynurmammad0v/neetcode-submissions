class Solution:
    # 1,2,4,6
    # 1,1,2,8
    # 48,24,6,1
    # 48,24,12,8

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i]*prefix

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix = nums[i]*postfix
        
        return res


