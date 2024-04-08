class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        cnt = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            for col in range(COLS):
                if row < 1 or col < 1:
                    continue
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True

        
        
