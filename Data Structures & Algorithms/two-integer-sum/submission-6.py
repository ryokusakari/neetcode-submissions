class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_target = {}

        for index, number in enumerate(nums): 
            difference = target-number
            if number not in to_target:
                to_target[difference] = index
            else:
                return [to_target.get(number),index]
        
