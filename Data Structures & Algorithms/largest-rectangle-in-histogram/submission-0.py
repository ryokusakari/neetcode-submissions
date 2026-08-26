class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        pointer = 0
        stack = []

        for index, height in enumerate(heights):
            if not stack: 
                stack.append((height, index))
            elif height > stack[-1][0]:
                stack.append((height, index))
            elif height < stack[-1][0]:
                while stack[-1][0] > height:
                    bar = stack.pop()
                    max_area = max(bar[0]*(index - bar[1]), max_area)
                    if not stack: 
                        break
                stack.append((height, bar[1]))
        
        while stack:
            bar = stack.pop()
            max_area = max(bar[0]*(len(heights) - bar[1]), max_area)
        
        return max_area
            






