class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for number in nums:
            res.append(prefix)
            prefix *= number

        postfix = 1
        for index in range(len(nums)-1,-1,-1):
            res[index] *= postfix
            postfix *= nums[index]

        return res

