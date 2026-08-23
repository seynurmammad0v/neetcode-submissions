class Solution:
    # Input: nums = [1,2,4,6]
    # prefixProduct = [1,1,2,8]
    # postfixProduct = [48,24,6,1]
    # Output: [48,24,12,8]    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProduct = [1] * len(nums)
        prefix = 1
        for index in range(len(nums)):
            prefixProduct[index] = prefix
            prefix *= nums[index]
        
        output  = [1] * len(nums)
        postfix = 1 
        for index in range(len(nums) - 1, -1, -1):
            output[index] = postfix * prefixProduct[index]
            postfix *= nums[index]
        return output


    