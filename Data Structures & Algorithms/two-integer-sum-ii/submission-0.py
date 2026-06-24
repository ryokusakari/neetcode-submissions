class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Sort list in descending order
        #Initialise pointers at start and end of the list
        #If the sum is larger than target, move reverse pointer down
        #If the sum is smaller than target, move forward pointer up
        #+1 to index and return

        numbers = sorted(numbers)
        fwd,rev = 0,len(numbers)-1
        while numbers[fwd] + numbers[rev] != target:
            if  numbers[fwd] + numbers[rev] > target:
                rev -= 1
            if numbers[fwd] + numbers[rev] < target:
                fwd += 1
        return [fwd+1,rev+1]



        