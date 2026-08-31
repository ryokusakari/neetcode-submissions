class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_dict = defaultdict(list)

        nums = set(nums)
        for number in nums:
            upper = consecutive_dict.pop((number+1), [number, number])
            lower = consecutive_dict.pop((number-1), [number, number])

            consecutive_dict[upper[1]] = [lower[0],upper[1]]
            consecutive_dict[lower[0]] = [lower[0],upper[1]]
        
        max_length = 0
        for sequence in consecutive_dict.values():
            max_length = max(sequence[1]-sequence[0]+1, max_length)
        
        return max_length