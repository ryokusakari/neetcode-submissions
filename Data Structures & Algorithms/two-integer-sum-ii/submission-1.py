class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Iterate through list 
        #For each number, calculate difference to target
        #Append difference to target and index to a hashmap
        #If difference exists in hashmap, return the integers as a list

        mem = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in mem: 
                return [min(i+1,mem[diff]),max(i+1,mem[diff])]
            else:
                mem[numbers[i]] = i+1

        