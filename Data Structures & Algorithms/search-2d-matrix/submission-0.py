class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        top = 0
        bottom = n_rows -1
        
        while top <= bottom:
            row = (top+bottom)//2
            if matrix[row][-1] < target:
                top = row+1
            elif matrix[row][0]>target:
                bottom = row -1
            else:
                break
        if top > bottom:
            return False
        
        row = (top+bottom) //2
        l = 0
        r = n_cols -1
        while l<=r:
            m=l + (r-l)//2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m+1
            else:
                return True
                
        return False