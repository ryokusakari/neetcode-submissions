class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, number in enumerate(nums):
            if number > 0:
                return result
        
            target = 0 - number
            l, r = index + 1, len(nums)-1

            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    triplet = [number, nums[l], nums[r]]
                    if triplet not in result:
                        result.append([number, nums[l], nums[r]])
                    l += 1
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1
        return result