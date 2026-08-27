class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: 
            return -1
        else:
            indeces = [i for i in range(len(nums))]
            while len(nums) > 1:
                left = nums[:len(nums)//2]
                right = nums[len(nums)//2:]
                if target in left:
                    nums = left
                    indeces = indeces[:len(indeces)//2]
                else:
                    nums = right
                    indeces = indeces[len(indeces)//2:]
                
            return indeces[0]