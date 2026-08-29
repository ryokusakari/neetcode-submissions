class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while r != l:
            mid = l + (r-l+1)//2
            if nums[mid] > nums[r]:
                if nums[0] <= target <= nums[mid-1]:
                    r = mid-1
                    break
                else:
                    l = mid
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                    break
                else:
                    r = mid-1

        while r != l:
            mid = l + (r-l+1)//2
            if target < nums[mid]:
                r = mid-1
            else:
                l = mid

        return r if nums[r] == target else -1       
        

