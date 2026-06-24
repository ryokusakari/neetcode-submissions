class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res, curr = 0,1
        print(nums)

        if len(nums) == 0:
            return 0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                res = max(curr,res)
                curr = 1
        res = max(curr,res)
        return res
                

        