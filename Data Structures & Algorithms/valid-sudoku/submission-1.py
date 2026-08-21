class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}

        for i in range(9):
            for j in range(9): 
              if board[i][j] == ".":
                continue
              row_key = f"row_{i}_{board[i][j]}" 
              column_key = f"col_{j}_{board[i][j]}" 
              section_key = f"sec_{i//3}_{j//3}_{board[i][j]}" 
              if row_key in seen or column_key in seen or section_key in seen:
                 return False
              seen[row_key] =1
              seen[column_key] =1
              seen[section_key] =1
        return True