class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        current = 1

        for index, number in enumerate(nums):
            result[index] *= current
            current *= number

        current = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= current
            current *= nums[i]

        return result


            
            




        