class Player:

    def __init__(self, marker, strategy):

        self.marker = marker
        self.strategy = strategy

    #given board and strategy, use strategy on current board state
    def make_move(self, board, alpha, table = None, move = None):
        if move:
            (i,j) = move
            board.state[i][j] = self.marker
            return
        else:
            # print(table)
            if table:

                return self.strategy(board, self.marker, alpha, table)
            
            else:

                return self.strategy(board, self.marker)
    
    def undo_move(self, board, move):

        (i,j) = move
        board.state[i][j] = None

        return