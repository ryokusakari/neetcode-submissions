class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1

        while l<=r:
            middle = (l+r)//2
            if target > matrix[middle][-1]:
                l = middle + 1
            elif target < matrix[middle][0]: 
                r = middle - 1
            else:
                break
        
        middle = (l+r)//2
        row = matrix[middle] 
        l,r = 0, len(row)-1    
        while l<=r:
            middle = (l+r)//2
            if row[middle] > target:
                r = middle - 1
            elif row[middle] < target:
                l = middle + 1
            else:
                return True
        
        return False
        
        