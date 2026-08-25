class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        frequency_array = [[] for _ in range(len(nums)+1)]
        res = []

        for number in nums:
            counter[number] = counter.get(number, 0) + 1
        
        for number, count in counter.items():
            frequency_array[count].append(number)
            
        i = -1

        while len(res) < k:
            if frequency_array[i]:
                res += frequency_array[i]
            i -= 1
        
        return res
            


