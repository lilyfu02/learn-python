from typing import List


class Solution():
    def captureRook(self, board: List[List[str]]) -> int:
        row, col = 0, 0
        theSum = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == 'R':
                    row = i
                    col = j
                    break
            else:
                continue
            break

        #up:
        for i in range(row,0,-1):
            if board[i][col] == 'p':
                theSum+=1
                break
            elif board[i][col] == 'B':
                break

        #down:
        for i in range(row,8):
            if board[i][col] == 'p':
                theSum+=1
                break
            elif board[i][col] == 'B':
                break

        #left:
        for i in range(col,0,-1):
            if board[row][i] == 'p':
                theSum+=1
                break
            elif board[row][i] == 'B':
                break

        #right:
        for i in range(col,8):
            if board[row][i] == 'p':
                theSum+=1
                break
            elif board[row][i] == 'B':
                break

        return theSum


boardchest = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", "p", "."],
              [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "p", ".", "."]]
solution = Solution()
print(solution.captureRook(boardchest))
