# def rotated(state):

# def is_similar(b1, b2):

def check_winners(state):
        winners = []
        # check rows
        for row in state:

            if row[0] == row[1] == row[2]:
                winners.append(row[0])
            
        # check cols
        for i in range(3):
            if state[0][i] == state[1][i] == state[2][i]:
                winners.append(state[0][i])
            
        # check diagonals
        if state[0][0] == state[1][1] == state[2][2]: 
            winners.append(state[0][0])
        
        if state[0][2] == state[1][1] == state[2][0]:
            winners.append(state[0][2])
        
        # check tie
        none_counter = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == None:
                    none_counter += 1

        if none_counter == 0 and len(winners) == 0:
            winners.append("TIE")
        
        if none_counter == 9:
            return None 
        
        if len(winners) == 0:
            return None
        else:
            return winners
        
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

def is_board(board):

    if len(board) != 3:
        print("1")
        return False
    
    for i in range(3):
        if len(board[i]) != 3:
            print("2")
            return False
    
    (xs, os) = count_markers(board)

    if abs(xs - os) > 1:
        print("3")
        return False

    if check_winners(board) != None:
        print("4")
        # print(check_winners(board))
        if len(check_winners(board)) > 1:
            return False
        

    return True
    
class Board:

    def __init__(self, state):
        # assert(is_board(state))
        if len(state) == 9:
            temp_row1 = []
            temp_row2 = []
            temp_row3 = []
            for i in range(3):
                temp_row1.append(i)
                temp_row2.append(i + 3)
                temp_row3.append(i + 6)
            self.state = [temp_row1, temp_row2, temp_row3]
        else:
            self.state = state
        assert(is_board(self.state))

    def check_finished(self):
        # check rows
        for row in self.state:

            if row[0] == row[1] == row[2]:
                return row[0]
            
        # check cols
        for i in range(3):

            if self.state[i][0] == self.state[i][1] == self.state[i][2]:
               return self.state[i][0]
            
        # check diagonals
        if self.state[0][0] == self.state[1][1] == self.state[2][2]: 
            return self.state[0][0]
        
        if self.state[0][2] == self.state[1][1] == self.state[2][0]:
            return self.state[0][2]
        
        # check tie
        none_counter = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == None:
                    none_counter += 1

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
