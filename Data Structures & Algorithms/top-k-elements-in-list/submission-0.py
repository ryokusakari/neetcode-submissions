class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Initialise a hashmap of integers and counts
        #Iterate through list 
        #If an integer is in the list, increase count by 1
        #If an integer is not in the list, add as new key
        #Sort hashmap by value and return top k keys as a list

        res = {}
        for i in nums:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1

        keys = list(res.keys())
        values = list(res.values())
        kvals = []
        for i in range(k):
            idx = values.index(max(values))
            kvals.append(keys[idx])
            keys.pop(idx)
            values.pop(idx)
        return kvals

        


        