class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 3:
            split = len(nums)//2
            if nums[split] > nums[-1]:
                nums = nums[split+1:]
            else:
                nums = nums[:split+1]
        return min(nums)