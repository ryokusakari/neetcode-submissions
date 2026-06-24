class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Sort list in ascending order
        #Initialise list of consecutive numbers
        #Intialise counter
        #Iterate through list
        #If next value is 1 greater than current, add 1 to counter
        #If next value is not 1 greater, append count to list and reset counter
        #Find maximum of list


        nums = list(set(nums))
        nums = sorted(nums)
        print(nums)
        if len(nums) == 0:
            return 0
        res,counter = [],1
        for i in range(len(nums)):
            if i == (len(nums)-1):
                res.append(counter)
                return max(res)
            if nums[i+1] == nums[i] + 1:
                counter += 1
            else:
                res.append(counter)
                counter = 1
        