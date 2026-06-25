class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for number in nums:
            counter[number] = counter.get(number, 0) + 1
  
        heap = []
        for number in counter.keys():
            heapq.heappush(heap, [counter[number],number])
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
                


        


            

        
        