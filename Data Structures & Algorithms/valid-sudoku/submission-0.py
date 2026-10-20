class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]


        for i in range(9):
            for j in range(9):
                number = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)
                if number != ".":
                    rows[i].append(number)
                    columns[j].append(number)
                    boxes[box_index].append(number)


        for i in range(9):
            if len(rows[i]) != len(set(rows[i])):
                return False

            if len(columns[i]) != len(set(columns[i])):
                return False

            if len(boxes[i]) != len(set(boxes[i])):
                return False

        return True
        