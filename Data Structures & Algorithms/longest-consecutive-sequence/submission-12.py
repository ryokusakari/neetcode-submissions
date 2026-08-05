class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = set(nums)
        consecutive_map = defaultdict(list)
        maximum = 0

        for number in nums: 
            if number+1 in consecutive_map and number-1 in consecutive_map:
                tail = consecutive_map.pop(number+1)
                head = consecutive_map.pop(number-1)
                consecutive_map[head[0]] = [head[0],tail[1]]
                consecutive_map[tail[1]] = [head[0],tail[1]]
            elif number+1 in consecutive_map:
                tail = consecutive_map.pop(number+1)
                consecutive_map[tail[1]] = [number,tail[1]]
                consecutive_map[number] = [number,tail[1]]
            elif number-1 in consecutive_map:
                head = consecutive_map.pop(number-1)
                consecutive_map[head[0]] = [head[0],number]
                consecutive_map[number] = [head[0],number]
            elif number not in consecutive_map:
                consecutive_map[number] = [number,number]

        for array in consecutive_map.values():
            maximum = max(maximum, array[1]-array[0]+1) 
        return maximum


    