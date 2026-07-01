class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = {}

        for index, number in enumerate(numbers):
            difference = target - number
            if difference in result:
                return [result[difference], index + 1]
            elif difference in numbers[index + 1:]:
                result = {number: index + 1}
