# find all moves possible from board
def find_free_moves(board):
    free_moves = []
    for i in range(3):
        for j in range(3):
            if board.state[i][j] == None:
                free_moves.append((i,j))

    return free_moves

# aggregate a list and return frequencies
def aggregate_and_print(list):
    D = {}
    for e in list:
        if D.get(e):
            D[e] += 1
        else:
            D[e] = 1

    res = ""
    for key in sorted(D.keys()):
        res += f"{key}: {D[key]}\n"

    print(res)
    return res

# aggregate a list in intervals and return frequencies
def aggregate_in_intervals_and_print(list, interval):
    LD = [list[interval * i: interval * (i+1)] for i in range(len(list)//interval)]
    for L in LD:
        aggregate_and_print(L)

    return


#check if all elements of a three element list are the same
def elements_eq(list):
    return list[0] == list[1] == list[2]