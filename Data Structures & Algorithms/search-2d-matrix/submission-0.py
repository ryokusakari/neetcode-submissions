class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full_list = []
        for row in matrix: 
            if not full_list:
                full_list = row
            else:
                full_list.extend(row)
        
        return target in full_list