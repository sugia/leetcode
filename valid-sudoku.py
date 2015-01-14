class Solution:
    #given a list of lists of strings, 9*9
    #return a bool
    def isValidSudoku(self, board):
        for i in range(9):
            que = []
            for j in range(9):
                que.append(board[i][j])
                if not self.cal(que):
                    return False
        
        for j in range(9):
            que = []
            for i in range(9):
                que.append(board[i][j])
                if not self.cal(que):
                    return False
        
        for x in range(3):
            for y in range(3):
                que = []
                for i in range(3):
                    for j in range(3):
                        que.append(board[x*3+i][y*3+j])
                if not self.cal(que):
                    return False
        return True
        
    def cal(self, que):
        can = set()
        for x in que:
            if x == '.':
                continue
            if x in can:
                return False
            can.add(x)
        return True
