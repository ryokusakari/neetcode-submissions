class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        r,l = 0,len(heights)-1

        while r < l:
            max_water = max(max_water, min(heights[r], heights[l])*(l - r))
            if heights[r] > heights[l]:
                l -= 1
            else:
                r += 1
            
        return max_water


