class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Iterate through list in descending order, find the product up to that number and input into list 
        #Reverse list so that it is in correct orientation
        #Iterate through list in ascending order and multiply the initial list by the new products

        res, curr = [1], 1
        
        nums = list(reversed(nums))
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            res.append(curr)
        
        curr = 1
        nums = list(reversed(nums))
        res = list(reversed(res))
        for i in range(1, len(nums)):
            curr *= nums[i-1]
            res[i] *= curr
        
        return res
            


        