class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]


        while len(nums) > 3:
            split = len(nums)//2
            if nums[0] > nums[split-1]:
                nums = nums[:split]
            else:
                nums = nums[split:]
        return min(nums)