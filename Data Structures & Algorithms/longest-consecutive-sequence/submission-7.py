class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(list(set(nums)))
        print(nums)
        counter, result = 1, 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                counter += 1
            else: 
                result = max(result, counter)
                counter = 1
        
        return max(result, counter)

        



    
        

