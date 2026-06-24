class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create hashmap memory
        #Iterate through list and memorise index + target - number
        #If the target matches number then return true
        #If iteration through list completes then return false

        mem = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in mem:
                return [mem[diff],i]
            mem[n] = i


        