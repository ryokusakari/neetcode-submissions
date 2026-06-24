class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialise hashmap
        #If key not in hashmap, create new 
        #If key in hashmap, increase value counter by 1
        #Order hashmap by value and return k most frequent keys

        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        res = {k:v for k,v in sorted(res.items(), key = lambda item: item[1], reverse = True)}
        return list(res.keys())[0:k]
