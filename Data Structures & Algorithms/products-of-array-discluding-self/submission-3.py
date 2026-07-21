class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, current = [1], 1
        for i in range(len(nums)-1):
            current *= nums[i]
            result.append(current)

        
        current = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= current
            current *= nums[i]

        return result




            
        