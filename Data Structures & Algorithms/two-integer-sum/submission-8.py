class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_memory = defaultdict(int)

        for index, number in enumerate(nums): 
            if number in target_memory:
                return [target_memory[number], index]
            target_memory[target - number] = index


