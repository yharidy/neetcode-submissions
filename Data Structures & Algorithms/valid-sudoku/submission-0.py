class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[] for i in range(9)]
        columns=[[] for i in range(9)]
        boxes=[[] for i in range(9)]
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val==".":
                    continue
                rows[i].append(val)
                     
                columns[j].append(val)
                box_idx = (i//3) *3 +(j//3)
                boxes[box_idx].append(val)
        for r in rows:
            if len(set(r)) < len(r):
                return False
        for c in columns:
            if len(set(c)) < len(c):
                return False
        for b in boxes:
            if len(set(b)) < len(b):
                return False
        return True
            