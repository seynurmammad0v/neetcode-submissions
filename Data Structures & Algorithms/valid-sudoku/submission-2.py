class Solution:
  # map 
  # row_2_5 = true
  # col_4_5 = true
  # cel_2_2_5 = true
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      seen = {}
      i, j = 0,0
      for i in range(9):
        for j in range(9):
          val = board[i][j]
          if val == ".":
            continue
          row_key = f"row_{i}_{val}"
          col_key = f"col_{j}_{val}"
          cell_key = f"cel_{i//3}_{j//3}_{val}"
          if row_key in seen or col_key in seen or cell_key in seen:
            return False
          seen[row_key] = True
          seen[col_key] = True
          seen[cell_key] = True
      return True