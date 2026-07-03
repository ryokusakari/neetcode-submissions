class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result, i, j = 0, 0, len(heights) - 1

        while i < j: 
            result = max(result, min(heights[i], heights[j])*(j - i))
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        
        return result


