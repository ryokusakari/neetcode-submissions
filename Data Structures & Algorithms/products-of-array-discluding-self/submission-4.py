class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, prefix = [1], 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            result.append(prefix)

        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result




            
        