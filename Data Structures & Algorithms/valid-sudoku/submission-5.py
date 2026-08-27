class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_counter = [set() for _ in range(9)]
        subset_counter = [set() for _ in range(9)]

        for i, row in enumerate(board):
            row_counter = set()

            for j, element in enumerate(row):
                if element == ".":
                    continue

                subset = i//3 + 3*(j//3)
                element = int(element)
                if element in row_counter or element in column_counter[j] or element in subset_counter[subset]:
                    return False
                else:
                    row_counter.add(element)
                    column_counter[j].add(element)
                    subset_counter[subset].add(element)
        
        return True
                
            
