from utils import elements_eq
# def rotated(state):

# def is_similar(b1, b2):

def check_winners(state):
    # assert(is_board(state))

    none_counter = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == None:
                none_counter += 1

    row1 = state[0]
    row2 = state[1]
    row3 = state[2]

    col1 = [state[i][0] for i in range(3)]
    col2 = [state[i][1] for i in range(3)]
    col3 = [state[i][2] for i in range(3)]

    diag1 = [state[i][i] for i in range(3)]
    diag2 = [state[i][2-i] for i in range(3)]

    winning_possibilities = [row1,row2,row3,col1,col2,col3,diag1,diag2]

    winners = []
    for winning_possibility in winning_possibilities:

        if elements_eq(winning_possibility) and winning_possibility[0] != None:
            winners.append(winning_possibility[0])
    
    if len(winners) != 0:
        return winners
    # no winners
    if none_counter == 0:
        return ["TIE"]

    return None

def count_markers(board):
    xs = 0
    os = 0

    for i in range(3):
        for j in range(3):
            if board[i][j]:
                if board[i][j] == 'X':
                    xs += 1
                else:
                    os += 1

    return xs, os

def is_board(board, debug_prints = False):

    if len(board) != 3:
        if debug_prints:

            print("1")
        return False
    
    for i in range(3):
        if len(board[i]) != 3:
            if debug_prints:

                print("2")
            return False
    
    (xs, os) = count_markers(board)

    if abs(xs - os) > 1:
        if debug_prints:

            print("3")
        return False

    winners = check_winners(board)

    if winners != None:
        # print(check_winners(board))
        none_counter = 0

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == None:
                    none_counter += 1
        
        
        if none_counter != 0 and len(check_winners(board)) > 1:
            if debug_prints:

                print("4")

            for i in range(1,len(winners)):
                if winners[i] != winners[i-1]:
                    return False
                
            return True
        

    return True
    
class Board:

    def __init__(self, state):
        # assert(is_board(state))
        if len(state) == 9:
            temp_row1 = []
            temp_row2 = []
            temp_row3 = []
            for i in range(3):
                temp_row1.append(state[i])
                temp_row2.append(state[i + 3])
                temp_row3.append(state[i + 6])
            self.state = [temp_row1, temp_row2, temp_row3]
        else:
            self.state = state

        # assert(is_board(self.state))

    def check_finished(self):
        # assert(is_board(self.state))

        none_counter = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == None:
                    none_counter += 1

        row1 = self.state[0]
        row2 = self.state[1]
        row3 = self.state[2]

        col1 = [self.state[i][0] for i in range(3)]
        col2 = [self.state[i][1] for i in range(3)]
        col3 = [self.state[i][2] for i in range(3)]

        diag1 = [self.state[i][i] for i in range(3)]
        diag2 = [self.state[i][2-i] for i in range(3)]

        winning_possibilities = [row1,row2,row3,col1,col2,col3,diag1,diag2]

        for winning_possibility in winning_possibilities:

            if elements_eq(winning_possibility) and winning_possibility[0] != None:
                return winning_possibility[0]
        
        # no winners
        if none_counter == 0:
            return "TIE"

        return None
    

    def __repr__(self):
        res = ""
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != None:
                    res += self.state[i][j]
                else:
                    res += 'N'

        return res
    
    def print(self):
        res = ""
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != None:
                    res += self.state[i][j]
                else:
                    res += 'N'
            res += '\n'
        print(res)
        return
