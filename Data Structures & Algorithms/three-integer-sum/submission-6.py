class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            l,r = i+1, len(nums)-1
            target = 0 - nums[i]

            while l<r:
                current_sum = nums[l] + nums[r]
                if current_sum < target: 
                    l +=  1
                elif current_sum > target:
                    r -= 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        output = []
        for result in results: 
            if result not in output: 
                output.append(result)
        
        return output



