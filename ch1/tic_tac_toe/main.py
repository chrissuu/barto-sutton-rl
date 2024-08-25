from player import Player
from board import Board
from utils import find_free_moves
from itertools import permutations
import random
import copy

B = Board([[None, None, None] for i in range(3)])

# random policy
def s1(board, marker):
    free_moves = find_free_moves(board)
    r = random.randint(0, len(free_moves) - 1)
    (i,j) = free_moves[r]

    board.state[i][j] = marker
    return

def update_table(board, board_next, alpha, table):
    table[board.__repr__()] +=  alpha * (table[board_next.__repr__()] - table[board.__repr__()])
    return

# returns a set of moves, sorted by increasing probability of winning
def get_move_distribution(board, free_moves, table, marker):
    temp_player = Player(marker)
    move_distribution = []

    for move in free_moves:
        (i,j) = move
        board_next = copy.deepcopy(board)
        temp_player.make_move(board_next,None,table,move)
        value = table[board_next.__repr__()]
        move_distribution.append((value, move))
        del board_next

    move_distribution = sorted(move_distribution, key = lambda x : x[1])
    return move_distribution

# given random variable R in [0, 100], picks an exploratory move with probability x
def pick_move(move_distribution, r, x):
    if r <= x:
        move_distribution.pop(-1)
        k = random.randint(0, len(move_distribution) - 1)
        return move_distribution[k][0]
    else:
        return move_distribution[-1][0]
    
# learnable policy
def s2(board, marker, alpha, table, x = 20):
    free_moves = find_free_moves(board)
    r = random.randint(0, 100)

    move_distribution = get_move_distribution(board, free_moves, table, marker)
    
    move = pick_move(move_distribution, r, x)

    temp_player = Player(marker)
    board_next = copy.deepcopy(board)
    temp_player.make_move(board_next, None, table, move)

    update_table(board, board_next, alpha, table)

    (i,j) = move
    board.state[i][j] = marker
    
    return

# initial table
def initial_table(m1, m2):

    table = {}

    games = get_all_games([m1, m2, None])
    print(len(list(games)))
    for game in list(len(games)):

        temp_B = Board(game)

        winner = temp_B.check_finished()

        if winner == "X":
            table[temp_B.__repr__()] = 0
        elif winner == "TIE":
            table[temp_B.__repr__()] = 0
        elif winner == "O":
            table[temp_B.__repr__()] = 1
        else:
            table[temp_B.__repr__()] = 0.5

    return table

def play_game(p1, p2, table):
    while B.check_finished() == None:

        p1.make_move(B, None, None)
        p2.make_move(B, 0.005, table)

    return B.check_finished()

def play_multiple_games(p1, p2, table, iterations):
    winners = []
    for i in range(iterations):
        winners.append(play_game(p1, p2, table))
    return winners

p1 = Player("X", s1)
p2 = Player("O", s2)

play_multiple_games(p1, p2, initial_table(p1.marker, p2.marker), 10)