class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_map = defaultdict(list)
        subset_map = defaultdict(list)

        for row in range(len(board)):
            row_map = [0]*9
            for column, number in enumerate(board[row]):
                if number == ".":
                    continue
                subset = (row - row % 3) + (column - column % 3)/3
                print(subset)
                if row_map[int(number) - 1] == 1:
                    return False
                elif number in column_map[column]:
                    return False
                elif number in subset_map[subset]:
                    return False
                else:
                    row_map[int(number)-1] = 1
                    column_map[column].append(number)
                    subset_map[subset].append(number)
        
        return True
