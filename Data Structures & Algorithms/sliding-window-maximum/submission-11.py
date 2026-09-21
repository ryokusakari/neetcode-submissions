from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        l = r = 0
        result = []

        while r < len(nums):
            while window and nums[window[-1]] < nums[r]: 
                window.pop()
            window.append(r)

            if window[0] < l:
                window.popleft()

            if r >= k-1:
                result.append(nums[window[0]])
                l += 1

            r += 1
        
        return result