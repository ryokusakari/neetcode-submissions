class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result, i, j = 0, 0, len(heights) - 1

        while i < j: 
            area = min(heights[i], heights[j])*(j - i)
            result = max(area, result)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return result


