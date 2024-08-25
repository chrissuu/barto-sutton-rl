def find_free_moves(board):
    free_moves = []
    for i in range(3):
        for j in range(3):
            if board.state[i][j] == None:
                free_moves.append((i,j))

    return free_moves
