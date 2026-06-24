class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Iterate through list with 2 pointers and sum
        #Check difference between sum and 0
        #If index is not i or j, then create list
        #If triplet not in res, add to res

        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = 0 - (nums[i] + nums[j])
                if diff in nums:
                    k = [x for x, n in enumerate(nums) if n == diff]
                    if i in k:
                        k.remove(i)
                    if j in k: 
                        k.remove(j)
                    if k:
                        for n in k:
                            temp = sorted([nums[i], nums[j], nums[n]])
                            if temp not in res:
                                res.append(temp)
        return res


