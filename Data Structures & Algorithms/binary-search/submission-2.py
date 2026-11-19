class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right: 
            middle = (left+right)//2
            value = nums[middle]
            if target < value:
                right = middle-1
            elif target > value:
                left = middle+1
            else: 
                return middle
        return left if nums[left] == target else -1
                
