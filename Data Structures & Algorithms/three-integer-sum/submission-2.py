class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result,i,j = [],0,1

        while i < len(nums) - 2:
            while j < len(nums) - 1:
                difference = 0 - (nums[i] + nums[j])
                if difference in nums[j + 1:]:
                    maximum = max([nums[i], nums[j], difference])
                    minimum = min([nums[i], nums[j], difference])
                    new_item = [minimum, 0 - (minimum + maximum), maximum]
                    if new_item not in result:
                        result.append(new_item)
                j += 1
            i += 1
            j = i + 1

        return result
