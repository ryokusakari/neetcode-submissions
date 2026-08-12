class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference_map = {}

        for index, number in enumerate(nums):
            if number not in difference_map:
                difference = target - number
                difference_map[difference] = index
            else:
                return [difference_map[number], index]

        