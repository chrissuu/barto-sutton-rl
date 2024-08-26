from player import Player
from board import Board, is_board
from utils import find_free_moves, aggregate_and_print
from itertools import permutations, product
import random
import copy


# random policy
def s1(board, marker):
    free_moves = find_free_moves(board)
    r = random.randint(0, len(free_moves) - 1)
    (i,j) = free_moves[r]

    board.state[i][j] = marker
    return

def update_table(board, board_next, alpha, table):
    # print("Table updated!")
    prev = f"{board.__repr__()}: {table[board.__repr__()]}"
    table[board.__repr__()] +=  alpha * (table[board_next.__repr__()] - table[board.__repr__()])
    curr = f"{board.__repr__()}: {table[board.__repr__()]}"
    # print(f"Table updated! {prev} -> {curr}")

    return

# returns a set of moves, sorted by increasing probability of winning
def get_move_distribution(board, free_moves, table, marker):
    temp_player = Player(marker, lambda x : x)
    move_distribution = []

    for move in free_moves:
        board_next = copy.deepcopy(board)
        temp_player.make_move(board_next,None,table,move)
        value = table[board_next.__repr__()]
        move_distribution.append((move, value))
        del board_next

    move_distribution = sorted(move_distribution, key = lambda x : x[1])
    return move_distribution

# given random variable R in [0, 100], picks an exploratory move with probability x
def pick_move(move_distribution, r, x):
    # exploratory move
    if r <= x:
        move_distribution.pop(-1)
        k = random.randint(0, len(move_distribution) - 1)
        return True, move_distribution[k][0]
    else:
        return False, move_distribution[-1][0]
    
# learnable policy, with x% of moves being exploratory -> 100-x % are exploitary
def s2(board, marker, alpha, table, x = 5):
    free_moves = find_free_moves(board)
    r = random.randint(0, 100)

    move_distribution = get_move_distribution(board, free_moves, table, marker)

    # print(move_distribution)
    is_exploratory, move = pick_move(move_distribution, r, x)

    if not is_exploratory:
        temp_player = Player(marker, lambda x: x)
        board_next = copy.deepcopy(board)
        temp_player.make_move(board_next, None, table, move)

        update_table(board, board_next, alpha, table)
        del board_next

    (i,j) = move
    board.state[i][j] = marker
    
    return


# initial table
def initial_table(m1, m2):

    table = {}

    games = list(product([m1,m2,None], repeat=9))
    # print(len(games))
    for game in games:
        temp_row1 = []
        temp_row2 = []
        temp_row3 = []
        for i in range(3):
            temp_row1.append(game[i])
            temp_row2.append(game[i + 3])
            temp_row3.append(game[i + 6])
        state = [temp_row1, temp_row2, temp_row3]
        
        if is_board(state):
            temp_B = Board(state)

            winner = temp_B.check_finished()

            if winner == "X":
                table[temp_B.__repr__()] = 0
            elif winner == "TIE":
                table[temp_B.__repr__()] = 0
            elif winner == "O":
                table[temp_B.__repr__()] = 1
            else:
                table[temp_B.__repr__()] = 0.5

    # print(len(table.keys()))
    return table

def play_game(p1, p2, table, board, alpha):
    # board.print()
    while board.check_finished() == None:

        p1.make_move(board, None, None)
        # board.print()
        if board.check_finished() != None:
            break

        p2.make_move(board, alpha, table)
        # board.print()
    return board.check_finished()

def play_multiple_games(p1, p2, table, iterations):
    board = Board([[None, None, None] for i in range(3)])

    winners = []
    alpha = 0.5
    for i in range(iterations):
        if iterations % 1000 == 0:
            alpha /= 1.3
        # game = play_game(p1, p2, table, board)

        winners.append(play_game(p1, p2, table, board, alpha))
        
        board = Board([[None, None, None] for i in range(3)])

    
    # print(winners)
    # print(table)
    return winners

p1 = Player("X", s1)
p2 = Player("O", s2)

winners = play_multiple_games(p1, p2, initial_table(p1.marker, p2.marker), 100000)

aggregate_and_print(winners)