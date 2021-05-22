class chessboard:
    def __init__(self, b):
        self.board = b

    def cost(self,bd):
        c = 0
        for i in range(0, 8):
            for j in range(i + 1, 8):
                if bd[i] == bd[j]:
                    c += 1
                cd = j - i
                if bd[i] == bd[j] - cd or bd[i] == bd[j] + cd:
                    c += 1
        return c

    def hill_climbing(self):
        neighbours = {}
        for col in range(0, 8):
            for row in range(0, 8):
                if self.board[col] == row:
                    continue
                new_board = list(self.board)
                new_board[col] = row
                neighbours[(col, row)] = self.cost(new_board)
        best = []
        current_heuristic = self.cost(self.board)
        for k, v in neighbours.items():
            if v < current_heuristic:
                current_heuristic = v
        for k, v in neighbours.items():
            if v == current_heuristic:
                best.append(k)
        col = best[0][0]
        row = best[0][1]
        self.board[col] = row
        return self.board

    def queens(self):
        moves = 0
        while self.cost(self.board) != 0:
            print("Board : ", self.board)
            print("Board violation : ", self.cost(self.board))
            self.board = self.hill_climbing()
            moves += 1

        print("Solution found in ", moves, " no of moves ")
        print("The solution is : ", self.board)
        print("The violations is : ", self.cost(self.board))


init_state = [1, 0, 5, 6, 3, 7, 2, 4]
cb=chessboard(init_state)
cb.queens()

'''
Board :  [1, 0, 5, 6, 3, 7, 2, 4]
Board violation :  4
Board :  [1, 1, 5, 6, 3, 7, 2, 4]
Board violation :  3
Board :  [1, 1, 0, 6, 3, 7, 2, 4]
Board violation :  2
Solution found in  3  no of moves 
The solution is :  [1, 5, 0, 6, 3, 7, 2, 4]
The violations is :  0
'''
