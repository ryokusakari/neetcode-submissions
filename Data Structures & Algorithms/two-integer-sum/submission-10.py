class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}

        for index, number in enumerate(nums):
            if number in target_map: 
                return [target_map[number], index]
            else:
                target_map[target-number] = index